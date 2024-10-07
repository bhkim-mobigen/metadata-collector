service_type = 'Altibase'

from test_metadata.metadata.database.custom.altibase.source import TestAltibaseSource
test = TestAltibaseSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestAltibaseSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
# test = TestAltibaseSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


