from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation


class TrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        data_ingestion = DataIngestion()
        ingestion_artifact = data_ingestion.run()

        data_validation = DataValidation(ingestion_artifact)
        validation_artifact = data_validation.run()
