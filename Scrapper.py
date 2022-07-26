#!/usr/bin/env python
# coding: utf-8


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv
import list_info as list_cases
import case_info as case

email = 'YOUR-EMAIL-HERE'
password = 'PASSWORD-HERE'
s = Service(ChromeDriverManager().install())
url_ = "http://securities.stanford.edu/filings.html?page="
pn = 1
max_pag_num=list_cases.get_total_page_number()
 
with open("Securities Class Action Filings 2022-01-08.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Filling Name", "Filing Date", "District Court", "Exchange", "Ticker", "Link", "docker","court","judge", "case_summary", "date_classperiod_start", "date_class_period_end", "case_status_info", "date_filing", "defendant_market_status", "defendant_headquarter", "defendant_industry", "defendant_sector"])
    while pn <= max_pag_num:
        all_line, driver = list_cases.get_all_cases_in_one_page(url_,pn,s,email,password)
        for oneline in all_line:
            # extract basic case variables from table
            name, date, court, exchange, ticker, link_case = list_cases.get_basic(oneline)
             # go inside each case and get more detailed variables. 
            docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector =case.extract_case_info(link_case, driver)
            # saves case information on a csv
            one = [name, date, court, exchange, ticker, link_case, docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector]
            writer.writerow(one)
            print(f"Case Saved: {name}")
            sleep(3)
        print(f"-- Complete: {pn} out of {max_pag_num} pages.--")
        driver.quit()
        pn += 1
print("Finish")
# %%
