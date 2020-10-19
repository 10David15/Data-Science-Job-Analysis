import scraper_Copy5 as scr 
import pandas as pd 

path= "C:/Program Files/chromedriver/chromedriver.exe"
df = scr.get_jobs('data scientist',200, True, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)
