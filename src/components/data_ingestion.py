import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split



@dataclass
class Dataingestionconfig:
    raw_data_path:str = os.path.join('artifacts','data.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')


class Dataingestion:

    def __init__(self):
        self.dataingestion_config = Dataingestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data integestion started...")

        try:
            df = pd.read_csv('src\Training_datafromDB\winequality-red.csv',sep=';')
            os.makedirs(os.path.dirname(self.dataingestion_config.train_data_path))
            
            df.to_csv(self.dataingestion_config.raw_data_path,index=False,header=True)
            logging.info("Raw data file created....")

            logging.info("Train test split initiated.....")

            train,test = train_test_split(df,test_size=0.3,random_state=42)

            train.to_csv(self.dataingestion_config.train_data_path,index=True,header=True)

            test.to_csv(self.dataingestion_config.test_data_path,index=True,header=True)

            logging.info("Data ingestion is completed....")

            return (
            self.dataingestion_config.train_data_path,
            self.dataingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException
        
if __name__ == "__main__":
    obj = Dataingestion()
    obj.initiate_data_ingestion()