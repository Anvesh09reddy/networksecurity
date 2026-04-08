from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        trainingpipleineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipleineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initialized DataIngestion class successfully.")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

