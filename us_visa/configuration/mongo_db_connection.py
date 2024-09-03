import pymongo
from us_visa.constants import *
from us_visa.execption import USvisaException
from us_visa.logger import logging
import sys

class MongoDBClient:
    client = None
    def __init__(self,database_name= DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGO_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f'Environment key {MONGO_URL_KEY} is not set')
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
            self.client =  MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('MongoDB connection successful')
        except Exception as e:
            raise USvisaException(e,sys)
            