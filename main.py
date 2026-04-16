from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
import sys
from networksecurity.components.model_trainer import ModelTrainer

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
        logging.info("Initializing DataTransformation class successfully.")
        data_transformation_config=DataTransformationConfig(training_pipeline_config=trainingpipleineconfig)
        data_transformation=DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data transformation completed successfully.")
        print(data_transformation_artifact)

        logging.info("Initializing ModelTrainer class successfully.")
        model_trainer_config=ModelTrainerConfig(training_pipeline_config=trainingpipleineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model training completed successfully.")
        print(model_trainer_artifact)


        



        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

