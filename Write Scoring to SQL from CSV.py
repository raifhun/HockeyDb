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

class ScoringEntry(Base):
    __tablename__="scoring"
    id=Column(Integer,primary_key=True)
    playerID=Column(String(25))
    year=Column(Integer)
    stint=Column(Integer)
    tmID=Column(String(5))
    lgID=Column(String(5))
    pos=Column(String(5))
    GP=Column(Integer)
    G=Column(Integer)
    A=Column(Integer)
    Pts=Column(Integer)
    PIM=Column(Integer)
    plusminus=Column(Integer)
    PPG=Column(Integer)
    PPA=Column(Integer)
    SHG=Column(Integer)
    SHA=Column(Integer)
    GWG=Column(Integer)
    GTG=Column(Integer)
    SOG=Column(Integer)
    PostGP=Column(Integer)
    PostG=Column(Integer)
    PostA=Column(Integer)
    PostPts=Column(Integer)
    PostPIM=Column(Integer)
    Postplusminus=Column(Integer)
    PostPPG=Column(Integer)
    PostPPA=Column(Integer)
    PostSHG=Column(Integer)
    PostSHA=Column(Integer)
    PostGWG=Column(Integer)
    PostSOG=Column(Integer)
    ClutchFactor=Column(String(50))
    
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

titleline=True
clutch_float=float
current_clutch=str()
RPPG=0
PPPG=0
#opens the csv, chops it up and packages it in above schema and adds it to the sql database, in this case also calculates clutchfactor and adds it as a parameter
with open(pathname+'\\Scoring.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if row[i]=='':
                row[i]=None
        if titleline==False:
            if row[25] != None and row[12] != None:
                RPPG=int(row[12])
                PPPG=int(row[25])
                if RPPG!=0 and PPPG!=0:
                    clutch_float=PPPG/RPPG
                    current_clutch=str(clutch_float)
            scoring_to_write=ScoringEntry(playerID=row[0],year=row[1],stint=row[2],tmID=row[3],lgID=row[4],pos=row[5],GP=row[6],G=row[7],A=row[8],Pts=row[9],PIM=row[10],plusminus=row[11],PPG=row[12],PPA=row[13],SHG=row[14],SHA=row[15],GWG=row[16],GTG=row[17],SOG=row[18],PostGP=row[19],PostG=row[20],PostA=row[21],PostPts=row[22],PostPIM=row[23],Postplusminus=row[24],PostPPG=row[25],PostPPA=row[26],PostSHG=row[27],PostSHA=row[28],PostGWG=row[29],PostSOG=row[30],ClutchFactor=current_clutch)
            session.add(scoring_to_write)
            current_clutch=None
        if titleline==True:
            titleline=False
    session.commit()
            
