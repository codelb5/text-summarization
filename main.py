from textSummarizer.logger import logger
from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)


STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} initiated <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
