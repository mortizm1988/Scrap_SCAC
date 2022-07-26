from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import re
import requests

def get_html(url,s,email,password):
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[2]/ul/li[6]/a[2]/strong').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[1]/input').send_keys(email)
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[2]/button[3]').click()
    sleep(3)
    html = driver.page_source
    #driver.quit()
    return html, driver
 
def get_total_page_number():
    req = requests.get("http://securities.stanford.edu/filings.html")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    page = str(soup.find("div", class_="span6"))
    pattern = r"\((?P<number>\d+)\)"
    object = re.search(pattern, page)
    num = int(object.group("number"))
    # print(num)
    page_number = num // 30 + 1
    return page_number
 
def get_all_cases_in_one_page(url_,pn,s,email,password):
    url = url_ + str(pn)
    # req = requests.get(url)
    # html = req.text
    html, driver = get_html(url,s,email,password)
    soup = BeautifulSoup(html, 'html.parser')
    # <tr class="table-link" page="filings" onclick="window.location='filings-case.html?id=107058'">
    all_line = soup.find_all("tr", class_="table-link", page="filings")
    return all_line, driver
 
def get_basic(one):
    pattern_link = r"id=(?P<id>\d*)"
    id = (re.search(pattern_link, str(one))).group("id")
    link_fix = "http://securities.stanford.edu/filings-case.html?id="
    link = link_fix + id
    info = one.find_all("td", class_="")
    name = info[0].get_text(strip=True)
    date = info[1].get_text(strip=True)
    court = info[2].get_text(strip=True)
    exchange = info[3].get_text(strip=True)
    ticker = info[4].get_text(strip=True)
    return name, date, court, exchange, ticker, link