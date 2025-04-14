from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_injection import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evulation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Surajjj0030/AI_DL-project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Surajjj0030"
os.environ["MLFLOW_TRACKING_PASSWORD"]="939c88a98ccc6f1d43ab2bcb1fb1fc1e8d854e56"

import mlflow
import os

# Set MLFLOW tracking uri
mlflow.set_tracking_uri("https://dagshub.com/Surajjj0030/AI_DL-project.mlflow")

# Set your dagshub crenditals (mlflow uses HTTP basic Auth)
os.environ["MLFLOW_TRACKING_USERNAME"]="Surajjj0030"
os.environ["MLFLOW_TRACKING_PASSWORD"]="939c88a98ccc6f1d43ab2bcb1fb1fc1e8d854e56"


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e