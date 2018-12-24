# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:06:16 2018

@author: Ketki
"""

import time
start = time.clock()
from bs4 import BeautifulSoup
import requests

url_tx = "https://www.monster.com/jobs/search/?cn=Bosch&where=Texas"
page = 0
url_tx = url_tx + "&stpage="  + str(page) + "&page=" + str(page)

monster_r = requests.get(url_tx)

monster_soup_tx = BeautifulSoup(monster_r.text, "html.parser")
print(monster_soup_tx.prettify())

   
print (time.clock() - start )

print(monster_r.status_code) # will be 200 if all is well 


job_title_tx = (monster_soup_tx.find_all('header', {'class' : 'card-header'})) 
    
job_titles_tx = []

for name in job_title_tx:
    title = (name.getText().strip("\n\r"))
    title = title.rstrip("\r\n")
    job_titles_tx.append(title)
    
    
    
   
job_place_tx = (monster_soup_tx.find_all('div', {'class' : 'location'}))

job_location_tx = []

for city in job_place_tx:
    place = (city.getText().strip("\r\n"))
    place = place.rstrip(" \r\n")
    job_location_tx.append(place)
    
  
org_tx = []    
company = (monster_soup_tx.find_all('div',{'class':'company'}))

for company_name in company:
    company = (company_name.getText().strip("\r\n"))
    company = company.rstrip("\r\n")
    org_tx.append(company)


duration_tx = []
time_tx = (monster_soup_tx.find_all('div',{'class':'meta flex-col'}))
   
for listing_tx in time_tx:
    time_tx = listing_tx.getText().strip("\r\n")
    time_tx = time_tx.rstrip("\n\n\nApplied\n\n\n\nSaved")
    duration_tx.append(time_tx)



################################# Illinois  #################################

url_il = "https://www.monster.com/jobs/search/?cn=Bosch&where=Illinois"
page = 0
url_il = url_il + "&stpage="  + str(page) + "&page=" + str(page)

monster_rm = requests.get(url_il)

monster_soup_il = BeautifulSoup(monster_rm.text, "html.parser")
print(monster_soup_il.prettify())

job_title_il = (monster_soup_il.find_all('header', {'class' : 'card-header'})) 

job_titles_il = []

for name in job_title_il:
    title = (name.getText().strip("\r\n"))
    title = title.rstrip("\r\n")
    job_titles_il.append(title)
    
    
   
job_place_il = (monster_soup_il.find_all('div', {'class' : 'location'}))

job_location_il = []

for city in job_place_il:
    place = (city.getText().strip("\r\n"))
    place = place.rstrip(' \r\n')
    job_location_il.append(place)
    
  
org_il = []    
company_il = (monster_soup_il.find_all('div',{'class':'company'}))

for company_name in company_il:
    company = (company_name.getText().strip("\r\n"))
    company = company.rstrip(' \r\n')
    org_il.append(company)

duration_il = []
time_il = (monster_soup_il.find_all('div',{'class':'meta flex-col'}))
   
for listing_il in time_il:
    time_il = listing_il.getText().strip("\r\n")
    time_il = time_il.rstrip("\n\n\nApplied\n\n\n\nSaved")
    duration_il.append(time_il)

#################  Michigan   #######################################

url_mi = "https://www.monster.com/jobs/search/?cn=Bosch&where=Michigan"
page = 0
url_mi = url_mi + "&stpage="  + str(page) + "&page=" + str(page)

monster_ri = requests.get(url_mi)

monster_soup_mi = BeautifulSoup(monster_ri.text, "html.parser")
print(monster_soup_mi.prettify())

for link_i in monster_soup_mi.find_all('a'):
    print(link_i.text)
    
job_title = (monster_soup_mi.find_all('header', {'class' : 'card-header'})) 

job_titles = []

for name in job_title:
    title = (name.getText().strip('\r\n'))
    title = title.rstrip(' \r\n')
    job_titles.append(title)
    
    
   
job_place = (monster_soup_mi.find_all('div', {'class' : 'location'}))

job_location_mi = []

for city in job_place:
    place = (city.getText().strip('\r\n'))
    place = place.rstrip(' \r\n')
    job_location_mi.append(place)
    
  
org_mi = []    
company = (monster_soup_mi.find_all('div',{'class':'company'}))

for company_name in company:
    comp = (company_name.getText().strip('\r\n'))
    comp = comp.rstrip(' \r\n')
    org_mi.append(comp)
    
    
duration_mi = []
time_mi = (monster_soup_mi.find_all('div',{'class':'meta flex-col'}))
   
for listing_mi in time_mi:
    time_mi = listing_mi.getText().strip("\r\n")
    time_mi = time_mi.rstrip("\n\n\nApplied\n\n\n\nSaved")
    duration_mi.append(time_mi)
    
import pandas as pd
import numpy as np
    
texas_df = pd.DataFrame([job_titles_tx, org_tx, job_location_tx, duration_tx]).T

texas_df['Salary'] = np.random.randint(40000, 75000, texas_df.shape[0])
Salary = texas_df['Salary']

Salary = Salary.tolist()
texas_df['url'] = "www.monster.com"
Url = texas_df['url']
Url = Url.tolist()

texas_bosch_data = pd.DataFrame([job_titles_tx, org_tx, Salary, job_location_tx,Url,duration_tx]).T


############ format Michigan data ###########

michigan_tf = pd.DataFrame([job_titles, org_mi, job_location_mi, duration_mi]).T
michigan_tf['Salary'] = np.random.randint(40000, 75000, michigan_tf.shape[0])
mi_Salary = michigan_tf['Salary']
mi_Salary = mi_Salary.tolist()
michigan_tf['url'] = "www.monster.com"
Url = michigan_tf['url']
Url = Url.tolist()

michigan_bosch_data = pd.DataFrame([job_titles, org_mi, mi_Salary,job_location_mi, Url, duration_mi]).T

#####3 format Illinois data ##### 

illinois_tf = pd.DataFrame([job_titles_il, org_il, job_location_il, duration_il]).T
illinois_tf['Salary'] = np.random.randint(40000, 75000, illinois_tf.shape[0])
li_Salary = illinois_tf['Salary']
li_Salary = li_Salary.tolist()
illinois_tf['url'] = "www.monster.com"
Url = illinois_tf['url']
Url = Url.tolist()
    
illinoise_bosch_data = pd.DataFrame([job_titles_il, org_il, li_Salary, job_location_il, Url, duration_il]).T



    
'''    
data = (monster_soup_il.find_all('div', {'class' : 'summary'}))

job_title = []
job_location = []
company = [] 
   
for jobs in data:
    job_title = jobs.find('h2', {'class':'title'})
    print(job_title.text)
    job_title.append(job_title.text)
    company = jobs.find('div',{'class':'company'})
    print(company.text)
    company.append(company.text)
    location = jobs.find('div',{'class':'location'})
    print(location.text)
    job_location.append(location.text)
 '''   
### cleaning the data #######

alljobs = pd.DataFrame([illinoise_bosch_data, michigan_bosch_data, texas_bosch_data])
    
    


illinoise_data = illinoise_bosch_data.replace([None],[''], regex = True)
texas_data = texas_bosch_data.replace([None],[''], regex = True)
michigan_data = michigan_bosch_data.replace([None],[''], regex = True)

illinoise_data = illinoise_data.replace(['/n'],[''], regex = True)
texas_data = texas_bosch_data.replace([None],[''], regex = True)
michigan_data = michigan_bosch_data.replace([None],[''], regex = True)

illinoise_data = illinoise_data.iloc[3:,]
    
michigan_data = michigan_data.iloc[3:,]
    
texas_data = texas_data.iloc[3:,]
'''
illinoise_data.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Project/my_programs/IL_bosch.csv")
texas_data.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Project/my_programs/TX_bosch.csv")
michigan_data.to_csv("C:/Users/Ketki/Desktop/My Library/SEM 3/SSDI/Project/my_programs/MI_bosch.csv")
'''

illinoise_data.to_csv("C:/Users/Rajan/GUI APP/Jo_Engine/IL_bosch.csv")
texas_data.to_csv("C:/Users/Rajan/GUI APP/Jo_Engine/TX_bosch.csv")
michigan_data.to_csv("C:/Users/Rajan/GUI APP/Jo_Engine/MI_bosch.csv")

print("Scrapping from monster is done !")


 
