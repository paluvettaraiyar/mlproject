import sys
import sqlite3
# import logger 

class DBconnection:

    columns = {
        'id':'INTEGER',
        'name':'TEXT'
    }
    def __init__(self):
        # logger.logging.info('Constructor is getting executed....')
        self.dbname = 'dbcon'
        
    def getDBconnection(self):
        connection = sqlite3.connect(self.dbname+'')
        # logger.logging.info('connection object..',connection)
        return connection
    
    def createTable(self):
        connection = self.getDBconnection()
        # exec = connection.execute('create table demo (id INTEGER,name TEXT)')
        # logger.logging.info('create table command is executed...',exec)



        

if __name__ == "__main__":
    # logger.logging.info('The Dbconnection class is started executing....')
    # print(sys.path)
    obj = DBconnection()
    obj.createTable()
    print("connection statrted")