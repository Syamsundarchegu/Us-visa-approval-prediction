import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from us_visa.data_access.usvisa_data import UsvisaData
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.execption import USvisaException
from us_visa.logger import logging
from us_visa.entity.artifact_entity import DataIngestonAtrifact
from pandas import DataFrame

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig= DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USvisaException(sys,e)
    def export_data_info_feature_store(self) -> DataFrame:
        try:
            logging.info("Exporting data from mongodb")
            usvisa_data= UsvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe : {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise USvisaException(sys,e)
        
    def split_data_as_train_test(self,dataframe:DataFrame) -> None:
        logging.info("Entered split_data_as_train_test method of Data_Ingestion class.")
        try:
            train_set,test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.trian_test_split_ration)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method of Data_Ingetration class.")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.mkdir(dir_path,exist_ok=True)
            
            logging.info(f"Exporting train and test file path")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            
            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise USvisaException(e , sys) from e
        
    def intiate_data_ingestion(self) -> DataIngestonAtrifact:
        logging.info("Entered iniate_data_ingestion method of Data_Ingestion calss")
        try:
            dataframe = self.export_data_info_feature_store()
            logging.info("Got the data from mongodb")
            self. split_data_as_train_test(dataframe)
            logging.info("Performed train test split on the dataset")
            logging.info("Exited initiate_data_ingestion method of Data_Ingestion Class")
            
            data_ingestion_artifact = DataIngestonAtrifact(train_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data ingenstion artifact : {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e,sys) from e