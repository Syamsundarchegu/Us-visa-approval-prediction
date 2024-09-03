import os
from datetime import datetime

DATABASE_NAME = 'US_VISA'
COLLECTION_NAME = 'visa_data'

MONGO_URL_KEY = os.getenv('MONGO_URL_KEY')

PIPELINE_NAME= 'usvisa'

ARTIFACT_DIR = 'artifact'

MODEL_FILE_NAME= 'model.pkl'

TARGET_COLUMN = 'case_status'

CURRENT_YEAR = datetime.today().year

PREPROCESSING_OBJECT_FILE_NAME= 'preprocessing.pkl'

FILE_NAME = 'usvisa.csv'

TRAIN_FILE_NAME= 'train.csv'

TEST_FILE_NAME= 'test.csv'




DATA_INGESTION_COLLECTION_NAME= 'visa_data'

DATA_INGESTION_DIR_NAME= 'data_ingestion'

DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'

DATA_INGESTION_INGESTED_DIR = 'ingested'


DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2