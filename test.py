import scraper as scr 
import pandas as pd 

path= "C:/Program Files/chromedriver/chromedriver.exe"

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
print("\n",country_ids)
region_id = input("Enter a a region id based on the reference list above :\n> ")
#num_jobs = input("Enter a number of jobs to scrape:\n> ") 
#verbose = input("Verbose? Enter True (for debugging) or False :\n> ") 
#path = input("Enter chromedriver path to exe:\n> ")
#slp_time = input("Enter a sleep time based on internet speed (seconds)[recommendation: 15]:\n> ")

# job_name, region_id, num_jobs, verbose, path, slp_time
sa_DA = scr.get_jobs(job_name, region_id, 100, False, path, 15)
print("\nStarting...")

print("\nCompleted.")
print("\nTest output (list length): ",str(len(sa_DA["Job Description"])))
print("\nTest output (set length): ",str(len(set(sa_DA["Job Description"]))))