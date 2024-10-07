from test_metadata.metadata.pipeline.test_pipeline_source import TestPipelineSource
class TestNifiSource(TestPipelineSource):

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
        from metadata.generated.schema.entity.services.connections.pipeline.nifiConnection import NifiConnection

        serviceConnection = PipelineConnection(config=NifiConnection(**{
            "type": "Nifi",
            "hostPort": "https://nifidev:8443",
            # "hostPort": "https://localhost:8443",
            "nifiConfig": {
                "username": "admin",
                "password": "ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB",
                "verifySSL": False,
            },
            "supportsMetadataExtraction": True,
        }))
        return serviceConnection
