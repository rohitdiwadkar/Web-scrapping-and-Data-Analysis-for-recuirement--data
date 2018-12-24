# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:11:17 2018

@author: Ketki
"""

import MySQLdb
import mysql.connector

conn = MySQLdb.connect( user = 'root', password = 'sesame', host = 'localhost', database = 'jobs')
mycursor = conn.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())

# Right now we do not have any table in jobs and thus the value is empty 

with open ('all_jobs.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'insert into AllJobs({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

print(mycursor.fetchall())



