import os
import yaml
from typing import List
from box.exceptions import BoxValueError
from pathlib import Path
from logger import logger
from ensure import ensure_annotations
from box import ConfigBox


@ensure_annotations
def read_yaml(filepath: Path):
    try:
        with open(filepath) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {filepath} loaded successfully..!")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {filepath} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def get_size(filepath: Path):
    size_in_kb = round(os.path.getsize(filepath) / 1024)

    return f"~ {size_in_kb} KB"


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {dir_path}")
