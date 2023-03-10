import sys
import sqlite3 
from src.logger import logging
from src.exception import CustomException
from src.utils import DBconnection


class DBopeartions:

    def __init__(self):
       
        print("This is a db connection string", DBconnection().get_DBconnection())



if __name__ == "__main__":
    DBopeartions()

        
