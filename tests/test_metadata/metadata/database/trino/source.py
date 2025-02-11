from test_metadata.metadata.database.test_database_source import TestDatabaseSource
class TestTrinoSource(TestDatabaseSource):

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
        from metadata.generated.schema.entity.services.connections.database.trinoConnection import \
            TrinoConnection

        serviceConnection = DatabaseConnection(config=TrinoConnection(**{
            "type": "Trino",
            "scheme": "trino",
            "username": "admin",
            "authType": None,
            "hostPort": "192.168.100.37:8090",
            "catalog": "hive",
        }))
        return serviceConnection
