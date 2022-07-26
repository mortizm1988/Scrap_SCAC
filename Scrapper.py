#!/usr/bin/env python
# coding: utf-8


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
import list_info as list_cases
import case_info as case

email = 'INSERT HERE'
password = 'INSERT HERE'
s = Service(ChromeDriverManager().install())
url_ = "http://securities.stanford.edu/filings.html?page="
pn = 1
max_pag_num=list_cases.get_total_page_number()
frame_all_cases = pd.DataFrame()
while pn <= max_pag_num:
    all_lines, driver = list_cases.get_all_cases_in_one_page(url_,pn,s,email,password)
    for oneline in all_lines:
        # extract basic case variables from table
        name, date, court, exchange, ticker, link_case = list_cases.get_basic(oneline)
        # go inside each case and get more detailed variables. 
        docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector = case.extract_case_info(link_case, driver)
        # saves case's information into the frame
        one = pd.DataFrame([name, date, court, exchange, ticker, link_case, docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector]).T
        frame_all_cases=pd.concat([frame_all_cases, one])
        #print(f"Case Saved: {name}")
        sleep(2)
    print(f"-- Complete: {pn} out of {max_pag_num} pages.--")
    driver.quit()
    pn += 1
print("DataFrame loaded")   
frame_all_cases.columns=["Filling Name", "Filing Date", "District Court", "Exchange", "Ticker", "Link", "docker","court","judge", "case_summary", "date_classperiod_start", "date_class_period_end", "case_status_info", "date_filing", "defendant_market_status", "defendant_headquarter", "defendant_industry", "defendant_sector"]
frame_all_cases.to_csv(data_scac,index=False, encoding='utf-8')    
print("DataFrame saved")
# %%
