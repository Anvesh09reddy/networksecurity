from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig
import sys

if __name__=="__main__":
    try:
        trainingpipleineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipleineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initialized DataIngestion class successfully.")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully.")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(training_pipeline_config=trainingpipleineconfig)
        data_validation=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        logging.info("Initialized DataValidation class successfully.")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed successfully.")
        print(data_validation_artifact)

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

