
from lxml import html, etree
import requests
import re
import os
import sys, traceback
import unicodecsv as csv
import argparse
import json

next_page=''
total_page=0
def parse(keyword, place, place_id, page_param):
    global next_page
    global total_page
    headers = {    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, sdch, br',
                'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
                'referer': 'https://www.glassdoor.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
    }

    
    try:
        job_litsting_url = 'https://www.glassdoor.com/Job/jobs.htm'
        # Form data to get job results-params for our job req(url n params vary based on req)
        data = {
            'suggestCount': 0,
            'suggestChosen': 'false',
            'clickSource': 'searchBtn',
            'typedKeyword' : keyword,
            'sc.keyword': keyword,
            'locT': 'S',
            'locId': place_id,
            'jobType': ''
        }

        job_listings = []
        if place_id:
            if page_param==1:
                response = requests.post(job_litsting_url, headers=headers, data=data)
            else:
                response = requests.post(next_page, headers=headers)                
            # extracting data from
            # https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=andr&sc.keyword=android+developer&locT=C&locId=1146821&jobType=
            parser = html.fromstring(response.text)
            # Making absolute url 
            base_url = "https://www.glassdoor.com"
            parser.make_links_absolute(base_url) #convert relative paths of all links absolute

            XPATH_ALL_JOB = '//li[@class="jl"]'
            XPATH_NAME = './/a/text()'
            XPATH_JOB_URL = './/a/@href'
            XPATH_LOC = './/span[@class="subtle loc"]/text()'
            XPATH_COMPANY = './/div[@class="flexbox empLoc"]/div/text()'
            XPATH_SALARY = './/span[@class="green small"]/text()'
            XPATH_PAGE_NO = './/div[@class="cell middle hideMob padVertSm"]/text()'
            XPATH_PAGE_LINK = './/li[@class="next"]'
            XPATH_PAGE_TIME = './/span[@class="minor"]/text()'

            try:
                raw_pageno = parser.xpath(XPATH_PAGE_NO)
                pageno=''.join(raw_pageno).strip() if raw_pageno else None
                total_page = int(pageno.replace('Page 1 of ',''))
            except:
                pass  
                #print('Exception in page number')                
            pages = parser.xpath(XPATH_PAGE_LINK)
            try:
                for page in pages:
                    raw_page_url = page.xpath(XPATH_JOB_URL)
                    next_page = raw_page_url[0] if raw_page_url else None
                    #print(raw_page_url)
            except:
                pass
                #print("Exception in page url")
            listings = parser.xpath(XPATH_ALL_JOB)
            for job in listings:
                raw_job_name = job.xpath(XPATH_NAME)
                raw_job_url = job.xpath(XPATH_JOB_URL)
                raw_lob_loc = job.xpath(XPATH_LOC)
                raw_company = job.xpath(XPATH_COMPANY)
                raw_salary = job.xpath(XPATH_SALARY)
                raw_date = job.xpath(XPATH_PAGE_TIME)
                print(raw_date)
                # Cleaning data
                job_name = ''.join(raw_job_name).strip('–') if raw_job_name else None
                job_location = ''.join(raw_lob_loc) if raw_lob_loc else None
                raw_state = re.findall(",\s?(.*)\s?", job_location)
                state = ''.join(raw_state).strip()
                raw_city = job_location.replace(state, '')
                city = raw_city.replace(',', '').strip()
                company = ''.join(raw_company).replace('–','')
                salary = ''.join(raw_salary).strip()
                job_url = raw_job_url[0] if raw_job_url else None
                if(len(raw_date) != 0):
                    date = raw_date[0]
                else:
                    date = "NIL"

                jobs = {
                    "Name": job_name,
                    "Company": company,
                    "State": state,
                    "City": city,
                    "Salary": salary,
                    "Location": job_location,
                    "Url": job_url,
                    "Posted Date":date
                }
                job_listings.append(jobs)

            return job_listings
        else:
            print("location id not available")
            traceback.print_exec(file=sys.stdout)

    except:
        pass
        #print("Failed to load locations")

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