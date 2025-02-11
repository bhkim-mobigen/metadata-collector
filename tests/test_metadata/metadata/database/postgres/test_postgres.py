from src.metadata.generated.schema.entity.services.databaseService import DatabaseServiceType
service_type = DatabaseServiceType.Postgres

from test_metadata.metadata.database.postgres.source import TestPostgresSource
# test = TestPostgresSource(service_type=service_type, sink_type="metadata-rest", sink_host='localhost')
# test = TestPostgresSource(service_type=service_type, sink_type="metadata-rest", sink_host='192.168.100.110')
test = TestPostgresSource(service_type=service_type, sink_type="file")

from test_metadata.metadata.common.test_metadata import MetadataExecutor
MetadataExecutor.execute(test)


