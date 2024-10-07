service_type = 'Tibero'

from test_metadata.metadata.database.custom.tibero.source import TestTiberoSource
test = TestTiberoSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestTiberoSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
# test = TestTiberoSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


