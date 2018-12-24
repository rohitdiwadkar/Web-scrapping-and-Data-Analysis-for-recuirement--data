1+1
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import ipython_bell
#print("done")

#""%matplotlib inline""
#%config InlineBackend.figure_format = 'svg'
# %config InlineBackend.figure_format = 'retina'\

#%bell



"Job Scrape Package."
import re
from datetime import datetime as dt
from datetime import timedelta as td
from urllib.request import urlopen as urlopen

from bs4 import BeautifulSoup as Soup

from matplotlib.ticker import MaxNLocator

import numpy as np

import pandas as pd
#from IPython.display import display

from selenium import webdriver


class JobScrape(object):
    """Job Scrape Object."""

    def __init__(self, query='Continental', max_days_posted=31,
                 region_city='Troy', region_state='MI',
                 local_city='Troy', sort_by='date',
                 job_type='fulltime'):
        """Initialize JobScrape object."""
        self.query = query
        self.region = region_city + ',+' + region_state
        self.sort_by = sort_by
        self.job_type = job_type
        self.max_days_posted = max_days_posted

        self.local_city = local_city
        self.jobs = pd.DataFrame()

        self.results()
        self.clean_results()
        self.filter_results()

        # Report job finished
        print('Job Scrape Finished.')

    def results(self):
        """Get job search results."""
        pd.set_option('max_colwidth', 500)    # to remove column limit

        # Generate base url string.
        url_count = ('http://www.indeed.com/jobs'
                     '?q={}'
                     '&jt={}'
                     '&sort={}'
                     '&l={}'
                     ).format(self.query,
                              self.job_type,
                              self.sort_by,
                              self.region
                              )

        # Make soup from first page.
        url_count_http = urlopen(url_count, timeout=10).read()
        soup_for_count = Soup(url_count_http, 'html.parser')

        # Get number of pages of results and display.
        results_number = soup_for_count.find('div', attrs={
            'id': 'searchCount'}).text
        number_of_results = int(results_number.lstrip().split(
            sep=' ')[3].replace(',', ''))
        print("Scraping " + str(number_of_results) + " results")

        # Loop through the pages, scraping 100 results at a time.
        i = int(number_of_results / 100)
        for page_number in range(i + 1):
            self.parse_page(page_number)

    def parse_page(self, page_number):
        """Parse a single page of 100 job listings."""
        url_results = ('http://www.indeed.com/jobs'
                       '?q={}'
                       '&jt={}'
                       '&sort={}'
                       '&l={}'
                       '&limit=100'
                       '&start={}'
                       ).format(self.query,
                                self.job_type,
                                self.sort_by,
                                self.region,
                                str(100 * page_number)
                                )

        url_results_http = urlopen(url_results, timeout=10).read()
        soup_for_results = Soup(url_results_http, 'html.parser')

        # Store the 100 job listings on the page
        results = soup_for_results.find_all('div', attrs={
            'data-tn-component': 'organicJob'})

        # Parse each job listing and add details to self.jobs DataFrame
        for elem in results:
            self.parse_page_elements(elem)

    def parse_page_elements(self, elem):
        """Add each element to self.jobs."""
        # print(elem)
        # print(elem.find('span', attrs={
        #     'itemprop':'name'}).text.strip())
        # remove this line after testing is finished
        comp_name = elem.find('span', attrs={
            'class': 'company'}).text.strip()
        job_title = elem.find('a', class_=''
                              'turnstileLink').attrs['title']
        # job_title = elem.find('a', attrs={'
        #   data-tn-element': "jobTitle"}).text.strip().capitalize()
        home_url = 'http://www.indeed.com'
        job_link = '%s%s' % (home_url, elem.find('h2', attrs={
            'class': 'jobtitle'}).find('a')['href'])
        # job_link = "https://www.indeed.com" + elem.find('h2',
        #     attrs={"class": "jobtitle"}).find('a')['href']
        job_addr = elem.find('span', attrs={
            'class': 'location'}).text.strip()
        job_posted = elem.find('span', attrs={
            'class': 'date'}).text
        job_id = elem.find('h2', attrs={
            'class': 'jobtitle'})['id']
        days_posted = self.return_days_posted(job_posted)

        # Create Javascript page scraper for use later
        # to parse job descriptions
        # scraper = JobDescScrape()
        # Job Description Parser
        job_desc = None
        # job_desc = scraper.scrape(job_link)

        comp_link_overall = elem.find('span', attrs={
            'itemprop': 'name'})
        # if company link exists, access it. Otherwise, skip.
        if comp_link_overall is not None:
            comp_link_overall = '%s%s' % (
                home_url, comp_link_overall.attrs['href'])
        else:
            comp_link_overall = None

        # add job info to jobs DataFrame
        self.jobs = self.jobs.append({'comp_name': comp_name,
                                      'job_title': job_title,
                                      'job_link': job_link,
                                      'job_posted': job_posted,
                                      'overall_link': comp_link_overall,
                                      'job_location': job_addr,
                                      'job_id': job_id,
                                      'days_posted': days_posted,
                                      'job_desc': job_desc
                                      }, ignore_index=True)

    def clean_results(self):
        """Clean duplicate results"""
        print('Cleaning and formatting')
        self.jobs.drop_duplicates(inplace=True)
        self.jobs['days_posted'] = self.jobs['days_posted'].apply(np.int64)
        self.jobs = self.jobs[['days_posted',
                               'job_title',
                               'job_location',
                               'comp_name',
                               'job_link',
                               'job_desc']]
        # format links into clickable hyperlinks
        # self.jobs['job_link'] =
        # self.jobs['job_link'].apply(lambda x:
        # '<a href="{}">{}</a>'.format(x,x))

    def filter_results(self):
        """Filter unwanted results"""
        print('Filtering')
        self.jobs = self.jobs[
            (self.jobs['days_posted'] <= self.max_days_posted) &
            (self.jobs['job_location'].str.contains(self.local_city, case=False)) &
            (self.jobs['job_title'].str.contains(' ll', case=False) == False) &
            (self.jobs['job_title'].str.contains(' lll', case=False) == False) &
            (self.jobs['job_title'].str.contains(' lv', case=False) == False) &
            (self.jobs['job_title'].str.contains(' v', case=False) == False) &
            (self.jobs['job_title'].str.contains(' II', case=False) == False) &
            (self.jobs['job_title'].str.contains(' III', case=False) == False) &
            (self.jobs['job_title'].str.contains(' IV', case=False) == False) &
            (self.jobs['job_title'].str.contains(' V', case=False) == False) &
            (self.jobs['job_title'].str.contains(' 2', case=False) == False) &
            (self.jobs['job_title'].str.contains(' 3', case=False) == False) &
            (self.jobs['job_title'].str.contains(' 4', case=False) == False) &
            (self.jobs['job_title'].str.contains(' 5', case=False) == False)
        ]

    def histogram(self):
        """Plot histogram of # of posts per day for the past 30 days."""
        import seaborn as sns
        import matplotlib.pyplot as plt

        plt.rcParams["axes.labelsize"] = 15

        print('Plotting histogram of postings')
        date_max_days_posted, date = self.date_ndays_ago(self.max_days_posted)

        # Make plot
        sns.set(style="white")

        bins = np.arange(0, self.max_days_posted + 1).astype(np.int64)

        ax = sns.countplot(x='days_posted',
                           data=self.jobs,
                           order=bins
                           )
        query_include = ' '.join(self.query.split('+-')[0].split('+'))
        query_exclude = "-" + ' -'.join(self.query.split('+-')[1:])
        title = (query_include.title() + ' Jobs'+ '\n( ' + query_exclude + ' )'+
                 '\n\n  City: ' + self.local_city + '    ' +
                 '\nRegion: ' + ' '.join(self.region.split('+')) +
                 '\n\nFrequency of Posts - %b %d')
        graph_title = (dt.strftime(date,
                                   dt.strftime(date_max_days_posted,
                                               title) + ' to %b %d'))
        xlabel = 'Number of days since posting'
        ylabel = 'Number of postings'
        ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
        ax.set_title(graph_title, fontsize=12)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)

        ax.text(0.99, 0.98, 'Total Jobs: '+str(self.jobs.shape[0]),
                horizontalalignment='right',
                verticalalignment='top',
                transform=ax.transAxes,
                fontsize=10)

        # Force y-axis to make tick marks at integers (overrides default float)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        # Make x-axis read from right to left
        ax.invert_xaxis()

        if self.max_days_posted > 10:
            plt.setp(ax.get_xticklabels()[1::2], visible=False)


        # Make ymax just a little bigger than max bin size
        xmin, xmax, ymin, ymax = ax.axis()
        ax.axis(ymax=1.05*ymax)

        # Show plot
        plt.show()

    @staticmethod
    def date_ndays_ago(n):
        '''Return date n-days ago and current date.'''
        current_date = dt.now()
        date_n_days_ago = current_date - td(days=n)
        return date_n_days_ago, current_date

    @staticmethod
    def return_days_posted(job_posted):
        """Convert non-numerical 'days posted' into a number."""
        days = job_posted.split()[0]
        if days == 'Just':
            return 0
        elif days == 'Today':
            return 0
        elif days == '30+':
            return 31
        else:
            return days


class JobDescScrape(object):
    """Job Description Object."""

    def __init__(self, link, width=1120, height=550):
        """Initialize PhantomJS driver to load JS redirect links."""
        self.link = link
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(width, height)
        self.job_desc = self.scrape_link()

    def scrape_link(self):
        """Scrape description from link."""
        print(self.link)
        self.driver.get(self.link)
        noodles = self.driver.page_source
        soup = Soup(noodles, 'html.parser')

        # Job Description Parser Settings between here and return
        # select tags based on base url
        if "icims.com" in self.link:
            print('on the right track')
            soup_filter = soup.findAll('div')
        else:
            soup_filter = soup.findAll(['p', 'li'])

        # join the array elements (i.e. the array of tags and contents)
        job_description = '\n\n'.join([s.get_text() for s in soup_filter
                                      if len(str(s.get_text())) > 1])

        # Cut junk after add based on base url
        if 'https://tableau' in self.link:
            job_description = job_description.split(
                'Tableau Software is a company on a mission', 1)[0]

        # removes any whitespace between two new lines
        re.sub(r'\n\s*\n', r'\n\n', job_description.strip(), flags=re.M)

        return job_description


if __name__ == '__main__':
    print('docstring')




