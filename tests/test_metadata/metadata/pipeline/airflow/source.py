from test_metadata.metadata.pipeline.test_pipeline_source import TestPipelineSource
class TestAirflowSource(TestPipelineSource):

    def getSourceConfig(self):
        from metadata.generated.schema.metadataIngestion.workflow import SourceConfig
        from metadata.generated.schema.metadataIngestion.pipelineServiceMetadataPipeline import PipelineServiceMetadataPipeline
        sourceConfig = SourceConfig(config=PipelineServiceMetadataPipeline(**{
            "type": "PipelineMetadata",
            "includeLineage": True,
            "includeOwners": True,
            "pipelineFilterPattern": {
                "includes": [],
                "excludes": []
            },
            "dbServiceNames": [],
            "markDeletedPipelines": True,
            "includeTags": True,

        }))
        return sourceConfig

    def getServiceConnection(self):
        from metadata.generated.schema.entity.services.pipelineService import PipelineConnection
        from metadata.generated.schema.entity.services.connections.pipeline.airflowConnection import AirflowConnection
        from metadata.generated.schema.entity.services.connections.database.postgresConnection import PostgresConnection

        serviceConnection = PipelineConnection(config=AirflowConnection(**{
            "type": "Airflow",
            "hostPort": "http://192.168.100.110:18080",
            "numberOfStatus": 10,
            "connection": PostgresConnection(**{
                "type": "Postgres",
                "scheme": "postgresql+psycopg2",
                "username": "airflow_user",
                "authType": {"password": "airflow_pass"},
                "hostPort": "192.168.100.110:15432",
                "database": "airflow_db",
                "ingestAllDatabases": False,
                "sslMode": "disable",
            }).dict(),
        }))
        return serviceConnection
