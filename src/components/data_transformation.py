import os 
import sys
import pandas as pd
import numpy as np
import dill

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig():
    preprocessing_pickle_path = os.path.join('artifacts','preprocessing.pkl')

class DataTransformation():

    def __init__(self):
        self.dataTransformation_config = DataTransformationConfig()
    

    def get_data_transfomration(self):

        numberical_variables = [
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "free sulfur dioxide",
            "total sulfur dioxide",
            "density","pH","sulphates","alcohol","quality"
        ]

        numerical_pipeline = Pipeline(

            steps = [
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
            ]
        )

        logging.info(f"this is numberical features:{numberical_variables}")

        preporcessor = ColumnTransformer(
            [
            ("numerical_pipeline",numberical_variables)
            ]

        )
        
        return preporcessor


    def initiate_data_transformation(self,train_path,test_path):

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        logging.info("Reading the training and testing data completed.")

        taget_column = "quality"

        preprocessing_object = self.get_data_transfomration()

        dependent_feature_train = train_df[taget_column]   
        independent_feature_train = train_df.drop(columns=[taget_column],axis=1)

        logging.info("Dependent and independent feature seperation for train")

        dependent_feature_test = test_df[taget_column]   
        independent_feature_test = test_df.drop(columns=[taget_column],axis=1)

        logging.info("Dependent and independent feature seperation for train")

        X_train = preprocessing_object.fit_transform(independent_feature_train)
        X_test = preprocessing_object.transform(independent_feature_test)

        train_array = np.c_[

            X_train,np.array(dependent_feature_train)
        ]
        test_array = np.c_[

            X_test,np.array(dependent_feature_test)
        ]
        savepickle(preprocessing_object)

        logging.info("creating the pickle file and saving the object in artifact")

        return(

            train_array,test_array
        )

    def savepickle(self,preprocessing_object):
        try:
            dir_name = os.path.dirname(self.dataTransformation_config.preprocessing_pickle_path)

            os.makedirs(dir_name,exist_ok=True)

            logging.info(f"The pickle path : {self.dataTransformation_config.preprocessing_pickle_path}")

            with open(self.dataTransformation_config.preprocessing_pickle_path,"wb") as f:
                dill.dump(preprocessing_object,f)
        except Exception as e:
            raise CustomException(e,sys)





    
    
        






