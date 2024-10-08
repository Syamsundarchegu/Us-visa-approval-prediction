import sys
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.artifact_entity import (DataIngestonAtrifact,DataValidationAtrifact)
from us_visa.entity.config_entity import (DataIngestionConfig,DataValidationConfig)
from us_visa.logger import logging
from us_visa.execption import USvisaException
from us_visa.components.data_validation import DataValidation

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()  # Replace this with actual data validation configuration.
    def start_data_ingestion(self):
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class.")
            logging.info("Getting data from mongodb.")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.intiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb.")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class.")
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e,sys) from e   
    def start_data_validation(self, data_ingestion_artifact: DataIngestonAtrifact) -> DataValidationAtrifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e    
    def run_pipline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise USvisaException(e,sys)
        