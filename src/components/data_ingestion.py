import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation


@dataclass
class DataIngestionConfig():
    
    raw_data_path=os.path.join('artifacts','data.csv')
    print(raw_data_path)
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')

class DataIngestion():

    def __init__(self) -> None:
        self.dataIngestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Reading the data using pandas")
            df = pd.read_csv('src\Training_datafromDB\winequality-red.csv',sep=';')

            train_df,test_df = train_test_split(df,test_size=0.3,random_state=42)

            os.makedirs(os.path.dirname(self.dataIngestionConfig.raw_data_path))
            
            train_df.to_csv(self.dataIngestionConfig.train_data_path,index=True,header=True)

            logging.info("created the train csv")

            test_df.to_csv(self.dataIngestionConfig.test_data_path,index=True,header=True)

            logging.info("created the test csv")

            df.to_csv(self.dataIngestionConfig.raw_data_path,index=True,header=True)

            logging.info("created the raw csv")

            return(
                self.dataIngestionConfig.train_data_path,
                self.dataIngestionConfig.test_data_path
                
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_path ,test_path = obj.initiate_data_ingestion()
    obj1 = DataTransformation()
    train,test = obj1.initiate_data_transformation(train_path,test_path)
    logging.info(train)
    logging.inf(test)
