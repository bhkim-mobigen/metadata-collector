from app.utils.client import SqlalchemyOrmClient, postgresql_url
from metadata.ingestion.sink.db import Metadata
from datetime import datetime

def get_client(db_host):
    db_conf = dict(host=f"{db_host}:15432",
                   user="openmetadata_user",
                   passwd="openmetadata_password",
                   db="openmetadata_db")
    client = SqlalchemyOrmClient(postgresql_url(**db_conf),
                                 charset='utf-8',
                                 sql_log=True)
    return client

def test_create_tables(db_host):
    client = get_client(db_host)
    client.create_all()

def test_insert_data(db_host):
    client = get_client(db_host)
    with client:
        metadata = Metadata(
            system_name="hive",
            type_name="hive_table",
            table_name="table_name",
            description="table_description",
            table_qualified_name="schema.table_name",
            db_name="",
            table_biz_meta={},
            column_meta={},
            mod_dt=datetime.now(),
            reg_dt=datetime.now(),
            sysnm="test_unit",
        )
        client.insert(metadata)
        client.commit()

def test_select_sql(db_host):
    client = get_client(db_host)
    with client:
        result = client.select_sql_dict("select * from public.tb_metadata")
        print(result)

def test_select_statement(db_host):
    client = get_client(db_host)
    with client:
        statement = client.create_select_statement(Metadata)
        result = client.select_sql_dict(statement)
        for r in result:
            print(r)

def test_select_filter(db_host):
    # 신청자 인증
    # - 사용자 조회 stmt
    from sqlmodel import col, and_
    db = get_client(db_host)
    with db:
        stmt = db.create_select_statement(Metadata,
                                          where=(and_(col(Metadata.id) == 'b7125114-5222-42b2-868a-0051e87e7fad'))
                                          )
        print(stmt)
        acct = db.select_sql_dict(stmt)

        print(acct)

if __name__ == '__main__':
    pass
    # test_create_tables('localhost')
    # test_create_tables('192.168.100.110')
    # test_insert_data('localhost')
    # test_select_sql('localhost')
    # test_select_statement('localhost')
    # test_select_filter('localhost')
