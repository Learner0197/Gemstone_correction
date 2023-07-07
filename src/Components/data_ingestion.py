# Data Ingestion - Reading the dataset

import os # use to create a path or to save a file
import sys # for system error
from src.logger import logging # importing exception and logger
from src.exception import CustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.Components.data_transformation import DataTransformation


## Initialize the data ingestion configuration
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(r"Notebook\Data\gemstone.csv")
            logging.info('Dataset read as pandas Dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30) 
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            
            logging.info('Ingestion if data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            
        except Exception as e:
            logging.info('Exception Occurd at Data Ingestion stage')
            raise CustomException(e,sys)
        

## run Data Ingestion

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_trasformation = DataTransformation()
    data = data_trasformation.initiate_data_transformation(train_data_path, test_data_path)
    #print(data)
    train_arr, test_arr, _ = data

