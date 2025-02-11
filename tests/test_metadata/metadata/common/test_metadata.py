from test_metadata.metadata.common.test_source import TestSource
class MetadataExecutor:

    @staticmethod
    def execute(testSource: TestSource):
        ########################################################
        # build metadata config
        ########################################################
        from metadata.generated.schema.metadataIngestion.workflow import OpenMetadataWorkflowConfig
        workflow_config: OpenMetadataWorkflowConfig = testSource.getMetadataWorkflowConfig()

        ########################################################
        # run metadata workflow
        ########################################################
        from metadata.workflow.metadata import MetadataWorkflow
        from metadata.workflow.workflow_output_handler import print_status
        workflow = MetadataWorkflow(workflow_config)
        workflow.execute()
        workflow.raise_from_status()
        print_status(workflow)
        workflow.stop()


