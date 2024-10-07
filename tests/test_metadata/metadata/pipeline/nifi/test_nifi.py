from metadata.generated.schema.entity.services.pipelineService import PipelineServiceType
service_type = PipelineServiceType.Nifi

from test_metadata.metadata.pipeline.nifi.source import TestNifiSource
# test = TestNifiSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestNifiSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
test = TestNifiSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)
