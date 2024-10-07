from metadata.generated.schema.metadataIngestion.workflow import Source
from metadata.generated.schema.metadataIngestion.workflow import SourceConfig
from metadata.generated.schema.entity.services.searchService import SearchConnection

from test_metadata.metadata.common.test_source import TestSource
class TestSearchSource(TestSource):

    def _getSource(self) -> Source:
        serviceConnection = self.getServiceConnection()
        sourceConfig = self.getSourceConfig()

        source = Source(type=self.service_type.value,
                        serviceName='-'.join(['Test', self.service_type.value]),  # 없으면 오류 발생
                        serviceConnection=serviceConnection,
                        sourceConfig=sourceConfig)

        return source

    def getSourceConfig(self) -> SourceConfig:
        return None

    def getServiceConnection(self) -> SearchConnection:
        return None
