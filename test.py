import scraper as scr 
import pandas as pd
import numpy as np

# Feature whereby users can scrape for data in their country of choice, 
# top X countries included according to GDP (PPP) ranking as of 2020, according t0
# http://statisticstimes.com/economy/projected-world-gdp-ranking.php  
# some regions excluded - glassdoor not listing / very few entries related to ds
country_ids = {"China":"4", 
               "United States":"1", 
               "India":"115", 
               "Japan":"123", 
               "Germany":"96", 
               "Russia":"205", 
               "Indonesia":"113", 
               "Brazi":"36", 
               "United Kingdom":"2", 
               "France":"86", 
               "Mexico":"169", 
               "Italy":"120", 
               "Turkey":"238", 
               "South Korea":"135", 
               "Spain":"219", 
               "Saudi Arabia":"207", 
               "Canada":"3", 
               "Egypt":"6", 
               "Islamic Republic of Iran":"118", 
               "Thailand":"229", 
               "Australia":"16", 
               "Poland":"193", 
               "Taiwan Province of China":"240", 
               "Nigeria":"177", 
               "Pakistan":"192", 
               "Malaysia":"170", 
               "Netherlands":"178", 
               "Bangladesh":"", 
               "Argentina":"", 
               "Vietnam":"", 
               "South Africa":"211", 
               "Colombia":"", 
               "United Arab Emirates":"6",  
               "Singapore":"3235921", 
               "Belgium":"25", 
               "Switzerland":"226", 
               "Sweden":"223", 
               "Romania":"203", 
               "Chile":"49", 
               "Hong Kong SAR":"2308631", 
               "Peru":"189", 
               "Austria":"18", 
               "Ireland":"70", 
               "Czech Republic":"77", 
               "Ukraine":"244", 
               "Norway":"180"}

job_name_ = input("Enter a search term:\n> ")
job_name = job_name_.replace(" ","+")
job_name.strip()
print(country_ids)
region_id = input("Enter a a region id based on the reference list above :\n> ")
#num_jobs = input("Enter a number of jobs to scrape:\n> ") 
#verbose = input("Verbose? Enter True (used for debugging) or False :\n> ") 
#path = input("Enter chromedriver path to exe:\n> ")
#slp_time = input("Enter a sleep time based on internet speed (seconds)[recommendation: 15]:\n> ")

path= "C:/Program Files/chromedriver/chromedriver.exe"

# For data collection use case: 3 job titles for 4 countries
sa_DA = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
sa_DA.to_csv('sa_DA.csv', index = False)
#sa_DS = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#sa_DS.to_csv('sa_DS.csv', index = False)
#sa_DE = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#sa_DE.to_csv('sa_DE.csv', index = False)

#us_DA = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#us_DA.to_csv('us_DA.csv', index = False)
#us_DS = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#us_DS.to_csv('us_DS.csv', index = False)
#us_DE = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#us_DE.to_csv('us_DE.csv', index = False)

#uk_DA = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#uk_DA.to_csv('uk_DA.csv', index = False)
#uk_DS = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#uk_DS.to_csv('uk_DS.csv', index = False)
#uk_DE = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#uk_DE.to_csv('uk_DE.csv', index = False)

#au_DA = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#au_DA.to_csv('au_DA.csv', index = False)
#au_DS = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#au_DS.to_csv('au_DS.csv', index = False)
#au_DE = scr.get_jobs(job_name, region_id, 1000, False, path, 15)
#au_DE.to_csv('au_DE.csv', index = False)
