from metadata.generated.schema.entity.services.pipelineService import PipelineServiceType
service_type = PipelineServiceType.Airflow

from test_metadata.metadata.pipeline.airflow.source import TestAirflowSource
test = TestAirflowSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestAirflowSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
# test = TestAirflowSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)

# todo: airflow 라이브러리 load 실패로 실행 안됨. airflow dag 에서 동작하도록 개발되어야 함.

