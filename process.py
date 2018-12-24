# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 00:08:29 2018

@author: Ketki
"""

import os                                                                       
from multiprocessing import Pool                                                
    
                                                                                                                                                       
processes = ('scrap.py','webScraper.py', 'webScrapper_Bosch.py',
             'webScrapper_DelphiTechnologies.py', 'webScrapper_Siemens.py',
             'scrape_monstor00.py')
                                    

                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=6)                                                        
pool.map(run_process, processes) 


'''
After running python programs,
Lets read the csvs and append them in one. 

import pandas as pd
import numpy as np 

conti_glass = pd.read_csv("")
bosch_glass = pd.read_csv("")
siemens_glass = pd.read_csv("")
delphi_glass = pd.read_csv("")
'''






