from metadata.generated.schema.entity.services.databaseService import DatabaseServiceType
service_type = DatabaseServiceType.Hive

from test_metadata.metadata.database.hive.source import TestHiveSource
# test = TestHiveSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestHiveSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
test = TestHiveSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


