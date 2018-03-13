Packages required: sqlalchemy,pymysql,csv,sys,os
Mysql server must be running

1) Downloaded
2) The schema files are included.
1) Each python script for populating the database will run as long as the csv file is in the same directory as the python file and you change the sql server location to your local mysql server(username and password).  It will create a database and/or the tables if they don't exist if connected to the mysql server.
2) I have written a fourth script for the scoring csv and it can also be run if the csv file is in the same directory.  I added a column for clutch factor as a measure of the change in ppg in the playoffs as opposed to regular season.
3)For Query a:

select * from coaches
order by year, w;

For Query b:
The following will return a list ascending order sorted by year and award count:

select playerID,year,count(*) as frequency
from AwardsPlayers
group by playerID,year
order by year,Count(*) ASC;

I don't know how to write this as a stored procedure, I don't have as good a level of experience with mysql.  However, I would pull the data from the query above into python in addition to doing a similar query to determine the coaches with the most wins to determine query c.  In my projects I mostly used python to do these types of comparisons but I have the feeling being more familiar with stored procedures would make the last two queries much easier.


