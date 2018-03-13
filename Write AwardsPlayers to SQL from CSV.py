from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey,func,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table
from sqlalchemy.sql.visitors import ClauseVisitor
import pymysql
from sqlalchemy import inspect
import csv
import sys, os

pathname = os.path.dirname(os.path.abspath( __file__ ))
Base=declarative_base()



#defining the schema manually
class AwardsPlayersEntry(Base):
    __tablename__="AwardsPlayers"
    id=Column(Integer,primary_key=True)
    playerID=Column(String(25))
    award=Column(String(25))
    year=Column(Integer)
    igID=Column(String(5))
    note=Column(String(25))
    pos=Column(String(5))



#Creates hockey database if there isn't one
engine=create_engine('mysql+pymysql://root:password@localhost:3306')
conn=engine.connect()
conn.execute("commit")
existing_databases=conn.execute("SHOW DATABASES;")
list_existing_databases=[d[0] for d in existing_databases]
if 'hockeydb' not in list_existing_databases:
    conn.execute("create database hockeydb")
conn.close()


#starts session and creates table if necessary
enginedb=create_engine('mysql+pymysql://root:password@localhost:3306/hockeydb')
Session=sessionmaker()
Session.configure(bind=enginedb)
session=Session()
Base.metadata.create_all(enginedb)


#opens the csv, chops it up and packages it in above schema and adds it to the sql database
titleline=True
with open(pathname+'\\AwardsPlayers.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if row[i]=='':
                row[i]=None
        if titleline==False:
            award_to_write=AwardsPlayersEntry(playerID=row[0],award=row[1],year=row[2],igID=row[3],note=row[4],pos=row[5])
            session.add(award_to_write)
            
        if titleline==True:
            titleline=False
    session.commit()