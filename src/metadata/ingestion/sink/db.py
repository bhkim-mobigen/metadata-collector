from typing import Optional, Dict, List, TypeVar
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

from metadata.config.common import ConfigModel
from metadata.ingestion.api.models import Either
from metadata.ingestion.api.steps import Sink
from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.utils.logger import get_log_name, ingestion_logger

from app.utils.dateutil import datetime_to_str
from datetime import datetime
import uuid

logger = ingestion_logger()

class DbSinkConfig(ConfigModel):
    host: str
    user: str
    passwd: str
    db: str

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
class Metadata(SQLModel, table=True):
    __tablename__ = "tb_metadata"

    id: str = Field(nullable=False, primary_key=True)
    system_name: Optional[str]
    type_name: Optional[str]
    table_name: Optional[str]
    description: Optional[str]
    table_qualified_name: Optional[str]
    db_name: Optional[str]
    table_biz_meta: Optional[Dict] = Field(sa_column=Column(JSONB))
    column_meta: Optional[List[Dict]] = Field(sa_column=Column(JSONB))
    create_time: Optional[str]
    update_time: Optional[str]
    mod_dt: str = Field(nullable=False, default=datetime_to_str(datetime.now()))
    reg_dt: str = Field(nullable=False, default=datetime_to_str(datetime.now()))
    sysnm: str = Field(nullable=False, default='sys')
    admin_chk_yn: str = Field(nullable=False, default="01")
    view_auth: str = Field(nullable=False, default="O")
    status: str = Field(nullable=False, default="ACTIVE")
    detail_description: Optional[str]
    reject_comment: Optional[str]
    requestor: Optional[str]

    class Config:
        arbitrary_types_allowed = True

from app.utils.client import SqlalchemyOrmClient, postgresql_url
from functools import singledispatchmethod
from metadata.generated.schema.api.services.createDatabaseService import CreateDatabaseServiceRequest
from metadata.generated.schema.api.data.createDatabase import CreateDatabaseRequest
from metadata.generated.schema.api.data.createDatabaseSchema import CreateDatabaseSchemaRequest
from metadata.generated.schema.api.data.createTable import CreateTableRequest
from metadata.generated.schema.api.services.createPipelineService import CreatePipelineServiceRequest
from metadata.generated.schema.api.data.createPipeline import CreatePipelineRequest
from metadata.generated.schema.api.services.createSearchService import CreateSearchServiceRequest
from metadata.generated.schema.api.data.createSearchIndex import CreateSearchIndexRequest
from metadata.generated.schema.entity.services.databaseService import DatabaseServiceType

C = TypeVar("C", bound=BaseModel)

class DbSink(Sink):
    """
    Sink implementation to store metadata in a file
    """

    config: DbSinkConfig

    def __init__(
        self,
        config: DbSinkConfig,
    ):
        super().__init__()
        self.config = config
        self.client = SqlalchemyOrmClient(postgresql_url(**self.config.dict()), charset='utf-8', sql_log=True)
        self.client.__enter__()
        self.items = []

    @classmethod
    def create(cls, config_dict: dict, _: OpenMetadata):
        config = DbSinkConfig.parse_obj(config_dict)
        return cls(config)

    @singledispatchmethod
    def _run(self, record: C, *_, **__) -> Either[str]:
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateDatabaseServiceRequest, *_, **__) -> Either[str]:
        if record.serviceType == DatabaseServiceType.CustomDatabase:
            scheme = record.connection.config.connectionOptions.__root__.get('scheme')
            if 'altibase' in scheme:
                self.system_name = "Altibase"
            elif 'tibero' in scheme:
                self.system_name = "Tibero"
        else:
            self.system_name = record.serviceType.value
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateDatabaseRequest, *_, **__) -> Either[str]:
        self.db_name = record.name.__root__
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateDatabaseSchemaRequest, *_, **__) -> Either[str]:
        self.schema_name = record.name.__root__
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateTableRequest, *_, **__) -> Either[str]:
        import json
        columns: list = [json.loads(column.json(), encoding='utf8') for column in record.columns]
        metadata = Metadata(
            id=str(uuid.uuid4()),
            system_name=self.system_name,
            type_name=record.tableType.value,
            table_name=record.name.__root__,
            description=record.description.__root__ if record.description else None,
            table_qualified_name=".".join([self.schema_name, record.name.__root__]),
            db_name=self.db_name,
            table_biz_meta={},
            column_meta=columns,
            mod_dt=datetime.now(),
            reg_dt=datetime.now(),
            sysnm="test_unit",
        )
        self.client.insert(metadata)
        self.client.commit()
        self.items.append(metadata)
        return Either(right=get_log_name(record))


    @_run.register
    def _(self, record: CreatePipelineServiceRequest, *_, **__) -> Either[str]:
        self.system_name = record.serviceType.value
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreatePipelineRequest, *_, **__) -> Either[str]:
        import json
        tasks: list = [json.loads(task.json(), encoding='utf8') for task in record.tasks]
        metadata = Metadata(
            id=str(uuid.uuid4()),
            system_name=self.system_name,
            type_name=None,
            table_name=record.name.__root__,
            description=record.displayName,
            table_qualified_name=None,
            db_name=None,
            table_biz_meta={},
            column_meta=tasks,
            mod_dt=datetime.now(),
            reg_dt=datetime.now(),
            sysnm="test_unit",
        )
        self.client.insert(metadata)
        self.client.commit()
        self.items.append(metadata)
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateSearchServiceRequest, *_, **__) -> Either[str]:
        self.system_name = record.serviceType.value
        return Either(right=get_log_name(record))

    @_run.register
    def _(self, record: CreateSearchIndexRequest, *_, **__) -> Either[str]:
        import json
        fields: list = [json.loads(field.json(), encoding='utf8') for field in record.fields]
        metadata = Metadata(
            id=str(uuid.uuid4()),
            system_name=self.system_name,
            type_name=None,
            table_name=record.name.__root__,
            description=record.displayName,
            table_qualified_name=None,
            db_name=None,
            table_biz_meta={},
            column_meta=fields,
            mod_dt=datetime.now(),
            reg_dt=datetime.now(),
            sysnm="test_unit",
        )
        self.client.insert(metadata)
        self.client.commit()
        self.items.append(metadata)
        return Either(right=get_log_name(record))


    def close(self):
        # self.client.commit()
        self.client.__exit__(None, None, None)
