from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity.config_entity import *

class ConfigurationManager:
    def __init__(self, config_filepath:str=CONFIG_FILEPATH, params_filepath:str=PARAMS_FILEPATH):
        self.config = read_yaml(filepath=config_filepath)
        self.params = read_yaml(filepath=params_filepath)

        create_directories(path_to_directories=[self.config.artifacts_root])


    def get_data_ingestion_config(self,)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories(path_to_directories=[config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir
            , source_url=config.source_url
            , local_data_file=config.local_data_file
            , unzip_dir=config.unzip_dir
        )

        return data_ingestion_config