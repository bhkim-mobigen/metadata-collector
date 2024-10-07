from metadata.generated.schema.entity.services.searchService import SearchServiceType
service_type = SearchServiceType.ElasticSearch

from test_metadata.metadata.search.elasticsearch.source import TestElasticSearchSource
# test = TestElasticSearchSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestElasticSearchSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
test = TestElasticSearchSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


