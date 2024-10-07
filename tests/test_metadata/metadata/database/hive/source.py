from test_metadata.metadata.database.test_database_source import TestDatabaseSource
class TestHiveSource(TestDatabaseSource):

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
                "includes": ['vslcm', 'vamrm'],
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
        from metadata.generated.schema.entity.services.connections.database.hiveConnection import \
            HiveConnection

        serviceConnection = DatabaseConnection(config=HiveConnection(**{
            "type": "Hive",
            "scheme": "hive",
            "username": "admin",
            "password": None,
            "hostPort": "192.168.100.35:10000",
            "auth": "NONE",
            "databaseName": "vslcm"
        }))
        return serviceConnection
