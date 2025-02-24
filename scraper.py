import bs4
import urllib
from urllib.request import urlopen
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(job_name, region_id, num_jobs, verbose, path, slp_time, filename):
            
    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+job_name+"&sc.keyword="+job_name+"&locT=N&locId="+region_id+"&jobType="
    #find number listings returned - modify value passed to function
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    soup = bs4.BeautifulSoup(urlopen(req),"html.parser")
    get = soup.find("div", { "class" : "hideHH css-19rczgc e15r6eig0" })
    results = []
    for i in get:
        if i.string is not None:
            results.append(i.string)
            
    max_jobs = int(results[0].split(" ")[0])
    print("Found a maximum of",max_jobs,"job postings.")
    if max_jobs < num_jobs: num_jobs = max_jobs
    print("Will get",num_jobs,"postings.\n")
    
    print("\nStarting...")
    options = webdriver.ChromeOptions()
    #uncomment below to scrape without a new Chrome window every time
    #options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:

        #let the page load. Change this number based on your internet speed.
        #or, wait until the webpage is loaded, instead of hardcoding
        time.sleep(slp_time)

        #test for sign-up prompt 
        try:
            driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(2)

        # remove sign-up
        try:
            driver.find_element_by_css_selector('[alt="Close"]').click()
        except NoSuchElementException:
            pass

        
        #each job in page
        job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:  
            try:
                print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
                if len(jobs) >= num_jobs:
                    break
    
                try :
                    job_button.click()
                except ElementNotInteractableException:
                    pass
                
                time.sleep(1)
                collected_successfully = False
                
                while not collected_successfully:
                    try:
                        company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                        location = driver.find_element_by_xpath('.//div[@class="location"]').text
                        job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                        job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                        collected_successfully = True
                    except:
                        time.sleep(5)
    
                try:
                    salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
                except NoSuchElementException:
                    salary_estimate = -1 #-1 used as not found value
                
                try:
                    rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
                except NoSuchElementException:
                    rating = -1 
    
                #debugging printouts
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))
    
                #Going to Company tab...
                #clicking on:
                #<div class="tab" data-tab-type="overview"><span>Company</span></div>
                try:
                    driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
    
                    try:
                        #<div class="infoEntity">
                        #    <label>Headquarters</label>
                        #    <span class="value">San Francisco, CA</span>
                        #</div>
                        headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                    except NoSuchElementException:
                        headquarters = -1
    
                    try:
                        size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                    except NoSuchElementException:
                        size = -1
    
                    try:
                        founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                    except NoSuchElementException:
                        founded = -1
    
                    try:
                        type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                    except NoSuchElementException:
                        type_of_ownership = -1
    
                    try:
                        industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                    except NoSuchElementException:
                        industry = -1
    
                    try:
                        sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                    except NoSuchElementException:
                        sector = -1
    
                    try:
                        revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                    except NoSuchElementException:
                        revenue = -1
    
                    try:
                        competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                    except NoSuchElementException:
                        competitors = -1
    
                except (NoSuchElementException, ElementClickInterceptedException):  #Rarely, some job postings do not have the "Company" tab.
                    headquarters = -1
                    size = -1
                    founded = -1
                    type_of_ownership = -1
                    industry = -1
                    sector = -1
                    revenue = -1
                    competitors = -1
    
                if verbose:
                    print("Headquarters: {}".format(headquarters))
                    print("Size: {}".format(size))
                    print("Founded: {}".format(founded))
                    print("Type of Ownership: {}".format(type_of_ownership))
                    print("Industry: {}".format(industry))
                    print("Sector: {}".format(sector))
                    print("Revenue: {}".format(revenue))
                    print("Competitors: {}".format(competitors))
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    
                #add job to jobs
                jobs.append({"Job Title" : job_title,
                "Salary Estimate" : salary_estimate,
                "Job Description" : job_description,
                "Rating" : rating,
                "Company Name" : company_name,
                "Location" : location,
                "Headquarters" : headquarters,
                "Size" : size,
                "Founded" : founded,
                "Type of ownership" : type_of_ownership,
                "Industry" : industry,
                "Sector" : sector,
                "Revenue" : revenue,
                "Competitors" : competitors})
                
            except (StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                continue
            
        #clicking on 'next page'
        try:
            driver.find_element_by_xpath('.//li[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
        
    print("\nCompleted.")
    return pd.DataFrame(jobs), pd.DataFrame(jobs).to_csv(filename+".csv", index = False)  #dictionary to DataFrame and as .csv
