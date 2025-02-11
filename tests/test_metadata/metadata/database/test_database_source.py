from src.metadata.generated.schema.entity.services.databaseService import DatabaseServiceType
from src.metadata.generated.schema.metadataIngestion.workflow import Source
from src.metadata.generated.schema.metadataIngestion.workflow import SourceConfig
from src.metadata.generated.schema.entity.services.databaseService import DatabaseConnection

from test_metadata.metadata.common.test_source import TestSource
class TestDatabaseSource(TestSource):

    def _getSource(self) -> Source:
        serviceConnection = self.getServiceConnection()
        sourceConfig = self.getSourceConfig()
        serviceTypeStr = self.service_type.value if type(self.service_type) == DatabaseServiceType else 'Custom'
        serviceNameStr = self.service_type.value if type(self.service_type) == DatabaseServiceType else self.service_type

        source = Source(type=serviceTypeStr,
                        serviceName='-'.join(['Test', serviceNameStr]),  # 없으면 오류 발생
                        serviceConnection=serviceConnection,
                        sourceConfig=sourceConfig)

        return source

    def getSourceConfig(self) -> SourceConfig:
        return None

    def getServiceConnection(self) -> DatabaseConnection:
        return None
