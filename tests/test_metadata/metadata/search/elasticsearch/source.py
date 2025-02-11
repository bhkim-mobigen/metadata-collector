from test_metadata.metadata.search.test_search_source import TestSearchSource
class TestElasticSearchSource(TestSearchSource):

    def getSourceConfig(self):
        from src.metadata.generated.schema.metadataIngestion.workflow import SourceConfig
        from src.metadata.generated.schema.metadataIngestion.searchServiceMetadataPipeline import SearchServiceMetadataPipeline
        sourceConfig = SourceConfig(config=SearchServiceMetadataPipeline(**{
            "type": "SearchMetadata",
            "searchIndexFilterPattern": {
                "includes": [],
                "excludes": []
            },
            "includeSampleData": True,
            "sampleSize": 10,
        }))
        return sourceConfig

    def getServiceConnection(self):
        from src.metadata.generated.schema.entity.services.searchService import SearchConnection
        from src.metadata.generated.schema.entity.services.connections.search.elasticSearchConnection import ElasticsearchConnection

        serviceConnection = SearchConnection(config=ElasticsearchConnection(**{
            "type": "ElasticSearch",
            "hostPort": "http://localhost:19200",
            "authType": None,
        }))
        return serviceConnection
