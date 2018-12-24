# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 02:18:44 2018

@author: rdas3
"""
#import urllib
import time
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv


#YOUR_STATE = 'North Carolina'

URL_TEMP = "http://www.indeed.com/jobs?q=continental%2C+bosch%2C+siemens%2C+delphie+technologies&l={}&start={}"

# loops through each city in the city list, and loops through each page with search results for that city
# 100 results per page, 10 pages per city --> 1000 job postings per city
# each time this cell is run the results list resets aka is empty (note this does not affect my dataframe)
# each job posting is appended to the results list (as html text)
# use append method, rather than list comprehension so data isn't overwritten
# sleep 1 sec between each url request
MAX_RESULTS_PER_CITY = 200 # Set this to a high-value (5000) to generate more results. 
# Crawling more results, will also take much longer. First test your code on a small number of results and then expand.
i = 0
RESULTS = []
DF_MORE = pd.DataFrame(columns=["Title","Location","Company","Salary", "Synopsis"])
for city in set(['IL', 'TX', 'MI']): #YOUR_STATE]):
    for start in range(0, MAX_RESULTS_PER_CITY, 10):
        # Grab the results from the request (as above)
        url = URL_TEMP.format(city, start) #Try changing this to look up states instead of cities
        # Append to the full set of results
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
        for each in soup.find_all(class_= "result" ):
            try: 
                Jobtype = each.find('div', attrs={'data-tn-component': 'organicJob'}).text.replace('\n', '') # To scrape only organic jobs and not sponsored ads
            except:
                title = "NaN"
            try: 
                title = each.find(class_='jobtitle').text.replace('\n', '')
            except:
                title = "NaN"
            try:
                location = each.find('span', {'class':"location" }).text.replace('\n', '')
            except:
                location = "Dearborn, MI"
            try: 
                company = each.find(class_='company').text.replace('\n', '')
            except:
                company = "NaN"
            try:
                job_posted = each.find(class_='date').text.replace('\n', '')
            except:
                job_posted = "NaN"
            try:
                salary = each.find(class_='no-wrap').text.replace('\n', '')
            except:
                salary = "None"
            try:
                synopsis = each.find('span', {'class':'summary'}).text.replace('\n', '')
            except:
                synopsis = "NaN"
            DF_MORE = DF_MORE.append({'days since post':job_posted,'Title':title, 'Location':location, 'Company':company, 'Salary':salary, 'Synopsis':synopsis}, ignore_index=True)
            i += 1
            if i % 1000 == 0:  #  counter to see how many. 
                print('You have ' + str(i) + ' RESULTS. ' + str(DF_MORE.drop_duplicates()) + " of these aren't rubbish.")
            DF_MORE.drop_duplicates(keep='first')
            #DF_MORE.to_csv(r'C:\Users\rdas3\Desktop\SSDI Continental Project\data_Siemens_15th_Test_Nov.csv', encoding='utf-8')
            DF_MORE.drop_duplicates(keep='first')
            OUTPATH = r'C:\Users\Rajan\GUI APP\Jo_Engine'
            filename = "Indeed_Job_Data_"+(time.strftime("%Y%m%d")+".csv")
            DF_MORE.to_csv(OUTPATH + "\\" + filename)
			
           # DF_MORE.to_csv(r'C:\Users\rdas3\Desktop\SSDI Continental Project\Siemens_15th__Nov.csv', encoding='utf-8')
				


    
    
    
    
    
    
    