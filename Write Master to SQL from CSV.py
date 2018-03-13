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



#defining the schema manually, alternatively could use automap base from database if you make the tables and seed them from mysql side or import the schema by using the csv wizard
class MasterEntry(Base):
    __tablename__="master"
    id=Column(Integer,primary_key=True)
    playerID=Column(String(25))
    coachID=Column(String(25))
    hofID=Column(String(25))
    firstName=Column(String(25))
    lastName=Column(String(25))
    nameNote=Column(String(50))
    nameGiven=Column(String(50))
    nameNick=Column(String(50))
    height=Column(Integer)
    weight=Column(Integer)
    shootCatch=Column(String(50))
    legendsID=Column(String(20))
    ihdbID=Column(Integer)
    hrefID=Column(String(25))
    firstNHL=Column(Integer)
    lastNHL=Column(Integer)
    firstWHA=Column(Integer)
    lastWHA=Column(Integer)
    pos=Column(String(5))
    birthYear=Column(Integer)
    birthMon=Column(Integer)
    birthDay=Column(Integer)
    birthCountry=Column(String(25))
    birthState=Column(String(25))
    birthCity=Column(String(25))
    deathYear=Column(Integer)
    deathMon=Column(Integer)
    deathDay=Column(Integer)
    deathCountry=Column(String(25))
    deathState=Column(String(5))
    deathCity=Column(String(25))



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
with open(pathname+'\\Master.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if row[i]=='':
                row[i]=None
        if titleline==False:
            master_to_write=MasterEntry(playerID=row[0],coachID=row[1],hofID=row[2],firstName=row[3],lastName=row[4],nameNote=row[5],nameGiven=row[6],nameNick=row[7],height=row[8],weight=row[9],shootCatch=row[10],legendsID=row[11],ihdbID=row[12],hrefID=row[13],firstNHL=row[14],lastNHL=row[15],firstWHA=row[16],lastWHA=row[17],pos=row[18],birthYear=row[19],birthMon=row[20],birthDay=row[21],birthCountry=row[22],birthState=row[23],birthCity=row[24],deathYear=row[25],deathMon=row[26],deathDay=row[27],deathCountry=row[28],deathState=row[29],deathCity=row[30])
            session.add(master_to_write)
            
        if titleline==True:
            titleline=False
    session.commit()