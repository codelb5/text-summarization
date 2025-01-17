import os
import zipfile
from urllib import request


from textSummarizer.utils.common import *
from textSummarizer.entity.config_entity import DataIngestionConfig
from textSummarizer.logger import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(
        self,
    ):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, filename=self.config.local_data_file
            )

            logger.info(f"{filename} downloaded..! with follwing info: \n{headers}")
        else:
            logger.info(
                f"File already exists..! Size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(
        self,
    ):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            logger.info(f"Extracting files into {unzip_path}")
            zip_ref.extractall(unzip_path)
