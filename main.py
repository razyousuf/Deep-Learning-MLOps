# 5. Create Endpoints

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # handles the data ingestion pipeline

# Define a human-readable name for pipeline stages
STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline() # Create pipeline object
    data_ingestion.main() # Run the main ingestion logic
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed\n\n <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e