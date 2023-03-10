import os
import sys
import sqlite3
import csv
from src.logger import logging
from src.exception import CustomException



class DBconnection:

    def __init__(self):
        self.dbname = 'dbcon'

    def get_DBconnection(self):

        connection = sqlite3.connect('src\DBConnection\sqllite_db'+'.db')
        return connection
    
    def create_table(self):
        try:

            connection = self.get_DBconnection()
            logging.info("Table creation process is started..")
            table_info = """ CREATE TABLE wine_data_red (
                fixed_acidity REAL,
                Fvolatile_acidity REAL,
                citric_acid REAL,
                residual_sugar REAL,
                chlorides REAL,
                free_sulfur_dioxide REAL,
                total_sulfur_dioxide REAL,
                density REAL,
                pH REAL,
                sulphates REAL,
                alcohol REAL,
                quality REAL
                ); """
            logging.info("Getting the cursor")
            cursor = connection.cursor()
            cursor.execute(table_info)
            logging.info("Table is created sucessfully")

        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_record(self):
        file = open('artifacts\data.csv')
        logging.info("Reading the raw data file....")
        read = csv.reader(file)
        connection = self.get_DBconnection()
        insert_query = "INSERT INTO wine_data_red (fixed_acidity,Fvolatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol,quality) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor = connection.cursor()
        logging.info("Insertion process is started...")
        cursor.executemany(insert_query,read)
        logging.info("Records are inserted in the table...")

            




if __name__=="__main__":
    obj = DBconnection()
    # obj.create_table()
    obj.insert_record()

        
 
