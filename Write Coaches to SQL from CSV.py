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
class CoachesEntry(Base):
    __tablename__="coaches"
    id=Column(Integer,primary_key=True)
    coachID=Column(String(20))
    year=Column(Integer)
    tmID=Column(String(5))
    IgID=Column(String(5))
    stint=Column(Integer)
    notes=Column(String(50))
    g=Column(Integer)
    w=Column(Integer)
    l=Column(Integer)
    t=Column(Integer)
    postg=Column(Integer)
    postw=Column(Integer)
    postl=Column(Integer)
    postt=Column(Integer)



#Creates hockey database if there isn't one
engine=create_engine('mysql+pymysql://root:password@localhost:3306')
conn=engine.connect()
conn.execute("commit")
existing_databases=conn.execute("SHOW DATABASES;")
list_existing_databases=[d[0] for d in existing_databases]
if 'hockeydb' not in list_existing_databases:
    conn.execute("create database hockeydb")
conn.close()


enginedb=create_engine('mysql+pymysql://root:password@localhost:3306/hockeydb')
Session=sessionmaker()
Session.configure(bind=enginedb)
session=Session()
Base.metadata.create_all(enginedb)
#opens the csv, chops it up and packages it in above schema and adds it to the sql database
titleline=True
with open(pathname+'\\Coaches.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if row[i]=='':
                row[i]=None
        if titleline==False:
            coaches_to_write=CoachesEntry(coachID=row[0],year=row[1],tmID=row[2],IgID=row[3],stint=row[4],notes=row[5],g=row[6],w=row[7],l=row[8],t=row[9],postg=row[10],postw=row[11],postl=row[12],postt=row[13])
            session.add(coaches_to_write)
            
        if titleline==True:
            titleline=False
    session.commit()
            
