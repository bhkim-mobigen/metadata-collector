from metadata.generated.schema.entity.services.databaseService import DatabaseServiceType
service_type = DatabaseServiceType.Trino

from test_metadata.metadata.database.trino.source import TestTrinoSource
# test = TestTrinoSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestTrinoSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
test = TestTrinoSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


