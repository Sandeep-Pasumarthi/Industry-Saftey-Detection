from src.components.data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        data_ingestion = DataIngestion()
        ingestion_artifact = data_ingestion.run()
