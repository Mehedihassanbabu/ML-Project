import os
import sys
import pymysql

import pickle
import numpy as np

from src.MLproject.exception import CustomException
from src.MLproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL Database Started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info(f"Connection Established {mydb}")
        df = pd.read_sql("SELECT * FROM students",mydb)
        print(df.head())
        
        return df
    
    except Exception as ex:
        raise CustomException(ex,sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True )
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
    