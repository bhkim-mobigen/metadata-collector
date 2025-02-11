from test_metadata.metadata.database.test_database_source import TestDatabaseSource
class TestTiberoSource(TestDatabaseSource):

    def getSourceConfig(self):
        from metadata.generated.schema.metadataIngestion.workflow import SourceConfig
        from metadata.generated.schema.metadataIngestion.databaseServiceMetadataPipeline import DatabaseServiceMetadataPipeline
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
                "includes": ['seoul_stg'],
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
        from metadata.generated.schema.entity.services.databaseService import DatabaseConnection
        from metadata.generated.schema.entity.services.connections.database.customDatabaseConnection import \
            CustomDatabaseConnection

        serviceConnection = DatabaseConnection(config=CustomDatabaseConnection(**{
            "type": "CustomDatabase",
            "sourcePythonClass": "metadata.ingestion.source.database.custom.tibero.metadata.TiberoSource",
            "connectionOptions": {
                "scheme": "tibero+pyodbc",
                "username": "seoul_stg",
                "password": "etl_staging",
                "odbcDnsName": "tibero6_seoul_dsn",
                "supportsProfiler": False,
                "supportsDBTExtraction": True,
                "supportsMetadataExtraction": True
            },
        }))
        return serviceConnection
