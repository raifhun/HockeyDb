import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

Coaches = pd.read_csv('C:/Users/Pone/Documents/RedHat Assessment/Goalies.csv', error_bad_lines=False)

enginedb = create_engine('mysql+pymysql://root:password@localhost:3306/hockeydb', echo=False)
Coaches.to_sql(name='sample_table_coaches', con=enginedb, if_exists='append', index=False)
