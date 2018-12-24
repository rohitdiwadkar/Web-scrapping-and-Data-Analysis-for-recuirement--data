# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 01:01:02 2018

@author: Ketki
"""
import pandas as pd
import numpy as np
from lxml import html, etree
import requests
import re
import os
import sys, traceback
import unicodecsv as csv
import argparse
import json
import __init__
import scrape_monster00
'''
from glassdoor import glass_Bosch
from glassdoor import glass_Conti
from glassdoor import glass_Delphi
from glassdoor import glass_Siemens
'''
import all_glassdoor
from all_glassdoor import parse
#import scrap
import math
import random
#import test_cases


total_page=0
# lets clean & consolidate the data 

if __name__ == "__main__":

    ''' eg-:python 1934_glassdoor.py "Android developer", "new york" '''

    scraped_data=[]
    keyword = "Bosch"
    place_ids = [1347, 302, 527]
    places = ["Texas", "Illinois", "Michigan"]
    
    if total_page == 0:
        total_page=10
    print("Fetching job details")
    for i in range(3):
        for page in range(1, total_page+1):
            data = parse(keyword, places[i], place_ids[i], page)
            #print(data)
            if data:
                scraped_data = scraped_data + data
            else:
                pass
                #print('Error in data rowss')
    
    print("Writing data to output file")

    with open('%s-job-results.csv' % (keyword), 'wb')as csvfile:
        fieldnames = ['Name', 'Company', 'State',
                      'City', 'Salary', 'Location', 'Url','Posted Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        if scraped_data:
            for data in scraped_data:
                if data:
                    writer.writerow(data)
                else:
                    pass
                    #print('Error in data row')
        else:
            print("Your search for %s, in %s does not match any jobs"%(keyword,places[0]))
            
if __name__ == "__main__":

    ''' eg-:python 1934_glassdoor.py "Android developer", "new york" '''

    scraped_data=[]
    keyword = "Continental"
    place_ids = [1347, 302, 527]
    places = ["Texas", "Illinois", "Michigan"]
    
    if total_page == 0:
        total_page=10
    print("Fetching job details")
    for i in range(3):
        for page in range(1, total_page+1):
            data = parse(keyword, places[i], place_ids[i], page)
            #print(data)
            if data:
                scraped_data = scraped_data + data
            else:
                pass
                #print('Error in data rowss')
    
    print("Writing data to output file")

    with open('%s-job-results.csv' % (keyword), 'wb')as csvfile:
        fieldnames = ['Name', 'Company', 'State',
                      'City', 'Salary', 'Location', 'Url','Posted Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        if scraped_data:
            for data in scraped_data:
                if data:
                    writer.writerow(data)
                else:
                    pass
                    #print('Error in data row')
        else:
            print("Your search for %s, in %s does not match any jobs"%(keyword,places[0]))
            
            
if __name__ == "__main__":

    ''' eg-:python 1934_glassdoor.py "Android developer", "new york" '''

    scraped_data=[]
    keyword = "Delphi Technologies"
    place_ids = [1347, 302, 527]
    places = ["Texas", "Illinois", "Michigan"]
    
    if total_page == 0:
        total_page=10
    print("Fetching job details")
    for i in range(3):
        for page in range(1, total_page+1):
            data = parse(keyword, places[i], place_ids[i], page)
            #print(data)
            if data:
                scraped_data = scraped_data + data
            else:
                pass
                #print('Error in data rowss')
    
    print("Writing data to output file")

    with open('%s-job-results.csv' % (keyword), 'wb')as csvfile:
        fieldnames = ['Name', 'Company', 'State',
                      'City', 'Salary', 'Location', 'Url','Posted Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        if scraped_data:
            for data in scraped_data:
                if data:
                    writer.writerow(data)
                else:
                    pass
                    #print('Error in data row')
        else:
            print("Your search for %s, in %s does not match any jobs"%(keyword,places[0]))
            
            
if __name__ == "__main__":

    ''' eg-:python 1934_glassdoor.py "Android developer", "new york" '''

    scraped_data=[]
    keyword = "Siemens"
    place_ids = [1347, 302, 527]
    places = ["Texas", "Illinois", "Michigan"]
    
    if total_page == 0:
        total_page=10
    print("Fetching job details")
    for i in range(3):
        for page in range(1, total_page+1):
            data = parse(keyword, places[i], place_ids[i], page)
            #print(data)
            if data:
                scraped_data = scraped_data + data
            else:
                pass
                #print('Error in data rowss')
    
    print("Writing data to output file")

    with open('%s-job-results.csv' % (keyword), 'wb')as csvfile:
        fieldnames = ['Name', 'Company', 'State',
                      'City', 'Salary', 'Location', 'Url','Posted Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
        writer.writeheader()
        if scraped_data:
            for data in scraped_data:
                if data:
                    writer.writerow(data)
                else:
                    pass
                    #print('Error in data row')
        else:
            print("Your search for %s, in %s does not match any jobs"%(keyword,places[0]))
# from Glassdoor: 
file1 = pd.read_csv('Bosch-job-results.csv')
file1 = file1.drop(['City','State'], axis=1)
file1['Salary'] = file1['Salary'].fillna(80000)
#file1['url']= "www.glassdoor.com"
file1 = pd.DataFrame(file1)
#file1.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Job_Engine/bosch.csv")

file2 = pd.read_csv('Siemens-job-results.csv')
file2 = file2.drop(['City','State'], axis=1)
file2['Salary'] = file2['Salary'].fillna(100000)
#file2['url']= "www.glassdoor.com"
file2 = pd.DataFrame(file2)
#file2.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Job_Engine/siemens.csv")

file3 = pd.read_csv('Continental-job-results.csv')
file3 = file3.drop(['City','State'], axis=1)
file3['Salary'] = file3['Salary'].fillna(50000)
#file3['url']= "www.glassdoor.com"
file3 = pd.DataFrame(file3)
#file3.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Job_Engine/conti.csv")

file4 = pd.read_csv('Delphi Technologies-job-results.csv')
file4 = file4.drop(['City','State'], axis=1)
file4['Salary'] = file4['Salary'].fillna(50000)
#file4['url']= "www.glassdoor.com"
file4 = pd.DataFrame(file4)
#file4.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Job_Engine/delphi.csv")

# from Monster : 

file5 = pd.read_csv('C:/Users/Rajan/GUI APP/Jo_Engine/IL_bosch.csv')
#file5 = file5.fillna("Bosch")
file5 = file5.iloc[:,1:]


file6 = pd.read_csv('C:/Users/Rajan/GUI APP/Jo_Engine/TX_bosch.csv')
#file6 = file6.fillna("Bosch")
file6 = file6.iloc[:,1:]



file7 = pd.read_csv('C:/Users/Rajan/GUI APP/Jo_Engine/MI_bosch.csv')
#file7 = file7.fillna("Bosch")
file7 = file7.iloc[:,1:]


# Combined data : 

all_data = np.vstack([file1, file2, file3, file4, file5, file6,file7])




#store it
all_data = pd.DataFrame(all_data)
all_data.columns = ['Job_Title','Company','Salary','Location','URL','Days posted']
all_data.to_csv("all_jobs.csv")

### clean the merged data ###


full_data = pd.read_csv('all_jobs.csv')
## making company names uniform ###

full_data['Company'] = full_data['Company'].replace("YoungCapital", "Bosch", regex = True)
full_data['Company'] = full_data['Company'].replace("IBM", "Bosch", regex = True)


#### maintain salary as numeric 

pay = full_data['Salary']
full_data['Salary'] = full_data['Salary'].replace('per hour', '', regex = True)
full_data['Salary']= full_data['Salary'].replace("k", "", regex = True)
full_data['Salary']= full_data['Salary'].replace("-", "", regex = True)
full_data['Salary']= full_data['Salary'].replace("\$", "", regex = True)

##### Changing location as per city and state in separate columns 

dfcleancsv = full_data['Location']
dfcleancsv = full_data['Location'].replace(" ","", regex = True)
dfcleancsv = dfcleancsv.str.split(",",expand = True)
full_data['City'] = dfcleancsv.iloc[:,0]
full_data['State'] = dfcleancsv.iloc[:,1]

merged_data = full_data[['Job_Title', 'Company', 'Salary', 'City', 'State', 'URL', 'Days posted']]
merged_data.to_csv("clean_all_jobs.csv")



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Usa2018$")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE cleanjobs")

with open ('all_jobs.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'insert into SQLNEW({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    #str.encode().decode()#
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()








