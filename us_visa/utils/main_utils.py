import os
import sys
import numpy as np
from pandas import DataFrame
import dill
import yaml

from us_visa.execption import USvisaException
from us_visa.logger import logging

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(  yaml_file )
    except Exception as e:
        raise USvisaException(e,sys) from e
    
def write_yaml_file(filepath:str,content:object,replace:bool=False):
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e,sys)
def load_object(filepath:str) ->object:
    logging.info("Entered the load_object method of utils")
    try:
        with open(filepath, 'rb') as file_obj:
            obj= dill.load(file_obj)
        logging.info("Exiting the load_object method of utils")
        return obj
    except Exception as e:
        raise USvisaException(e,sys) from e
    
    
def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dirpath = os.path.dirname(file_path)
        os.makedirs(dirpath, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e,sys) from e
    
def load_numpy_array_data(file_path:str) -> np.array:
    try:
        with open(file_path, 'rb') as file_obj:
            array = np.load(file_obj)
        return array
    except Exception as e:
        raise USvisaException(e,sys) from e
    
def save_object(file_path:str,obj:object):
    logging.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exiting the save_object method of utils")
    except Exception as e:
        raise USvisaException(e,sys) from e
    

    