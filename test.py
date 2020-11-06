# known issue: stops scraping at certain company tabs
# workaround: this is bypassed by manually clicking on the 'Job'
# tab of the posting it paused at, then resumes as normal; 
# also volatile when tested to scrape for large numbers of 
# job postings (above 800), may vary according to internet speed

import scraper as scr 
import os

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

# chromedriver download: (add directory as input after running)
# https://chromedriver.chromium.org/downloads
# my chromedriver path - "C:/Program Files/chromedriver/chromedriver.exe"

# user inputs
job_name_ = input("Enter a job search term:\n> ")
job_name_.strip()
job_name = job_name_.replace(" ","+")
print("\n",country_ids)
region_id = input("Enter a a region id based on the reference list above (: maps the pairs):\n> ")
num_jobs = int(input("Enter a number of jobs to scrape:\n> "))
path = input("Enter chromedriver path to exe (recent chromedriver installation is required):\n> ")
slp_time = int(input("Enter a sleep time based on internet speed (seconds)[recommendation: 15]:\n> "))
wd = os.getcwd()
filename = input("Enter file name to save as. The result will be also be saved as a .csv file in:\n"+wd+"\n\n> ")

# rename dataframe below if required
# verbose set as False, make True for debugging
my_data_frame = scr.get_jobs(job_name, region_id, num_jobs, False, path, slp_time, filename)
# my_data_frame.to_csv(filename+".csv", index = False)























