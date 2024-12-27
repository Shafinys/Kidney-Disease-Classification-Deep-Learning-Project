import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
import base64
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns the content as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 


def create_directories(path_to_directories: list, verbose=True):
  """create list of directories"""
  for path in path_to_directories:
      os.makedirs(path, exist_ok=True)
      if verbose:
          logger.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict):
    """save json data"""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """load json data"""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

def save_bin(data: Any, path: Path):
    """save binary data"""
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

def load_bin(path: Path) -> Any:
    """load binary data"""
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

def get_size(path: Path) -> str:
    """get size in KB"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB" 


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
    return f"Decoded image {fileName}"    

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

