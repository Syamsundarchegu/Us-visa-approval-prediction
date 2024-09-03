from us_visa.execption import USvisaException
from us_visa.logger import logging
import os
import sys
import pandas as pd
from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from typing import Optional
import numpy as np

class UsvisaData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
        except Exception as e:
            raise USvisaException(sys,e)
    def export_collection_as_dataframe(self, collection_name:str,database:Optional[str]=None):
        try:
            if database is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns.to_list():
                df = df.drop(columns=['_id'],axis=1)
            df.replace({'na':np.nan},inplace=True)
            return df
        except Exception as e:
            raise USvisaException(sys,e)
    