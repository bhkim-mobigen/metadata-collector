from test_metadata.metadata.database.test_database_source import TestDatabaseSource
class TestPostgresSource(TestDatabaseSource):

    def getSourceConfig(self):
        from src.metadata.generated.schema.metadataIngestion.workflow import SourceConfig
        from src.metadata.generated.schema.metadataIngestion.databaseServiceMetadataPipeline import DatabaseServiceMetadataPipeline
        sourceConfig = SourceConfig(config=DatabaseServiceMetadataPipeline(**{
            "type": "DatabaseMetadata",
            "markDeletedTables": False,
            "markDeletedStoredProcedures": False,
            "includeTables": True,
            "includeViews": True,
            "includeTags": False,
            "includeStoredProcedures": False,
            "queryLogDuration": 1,
            "queryParsingTimeoutLimit": 300,
            "useFqnForFiltering": False,
            "schemaFilterPattern": {
                "includes": [],
                "excludes": []
            },
            "tableFilterPattern": {
                "includes": [],
                "excludes": []
            },
            "databaseFilterPattern": {
                "includes": [],
                "excludes": []
            }
        }))
        return sourceConfig

    def getServiceConnection(self):
        from src.metadata.generated.schema.entity.services.databaseService import DatabaseConnection
        from src.metadata.generated.schema.entity.services.connections.database.postgresConnection import \
            PostgresConnection

        serviceConnection = DatabaseConnection(config=PostgresConnection(**{
            "type": "Postgres",
            "scheme": "postgresql+psycopg2",
            "username": "postgres",
            "authType": {"password": "postgres"},
            "hostPort": "192.168.100.34:5432",
            "database": "iwdf",
        }))
        return serviceConnection
