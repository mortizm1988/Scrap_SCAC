
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def extract_case_info(link,driver):    
    driver.get(link)
    docker=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[3]/div[2]/div[2]").text
    court=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[3]/div[2]/div[1]").text
    judge=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[3]/div[2]/div[3]").text
    date_classperiod_start=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[3]/div[3]/div[2]").text
    date_class_period_end=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[3]/div[3]/div[3]").text
    case_summary=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[1]/summary/div[3]/div").text
    case_status_info=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[1]/summary/p[1]").text
    date_filing=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[1]/summary/p[2]").text
    defendant_market_status=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[2]/div[3]/div[3]").text
    defendant_headquarter=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[2]/div[2]/div[3]").text
    defendant_industry=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[2]/div[2]/div[2]").text
    defendant_sector=driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/content/section[2]/div[2]/div[1]").text
    ## cleaning text
    docker=docker.replace("DOCKET #: ","")
    court=court.replace("COURT: ","")
    judge=judge.replace("JUDGE:","")
    date_classperiod_start=date_classperiod_start.replace("CLASS PERIOD START:","")
    date_class_period_end=date_class_period_end.replace("CLASS PERIOD END: ","")
    case_status_info=case_status_info.replace("Case Status:    ","")
    date_filing=date_filing.replace("Filing Date: ","")
    defendant_market_status=defendant_market_status.replace("Market Status: ","")
    defendant_headquarter=defendant_headquarter.replace("Headquarters: ","")
    defendant_industry=defendant_industry.replace("Industry: ","")
    defendant_sector=defendant_sector.replace("Sector: ","")
    return docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector

if __name__ == '__main__':
    s = Service(ChromeDriverManager().install())
    link = "https://securities.stanford.edu/filings-case.html?id=107979"
    email = 'marcelo.ortizm@upf.edu'
    password = '@Holanda2020'
    driver = webdriver.Chrome(service=s)
    docker,court,judge, case_summary, date_classperiod_start, date_class_period_end, case_status_info, date_filing, defendant_market_status, defendant_headquarter, defendant_industry, defendant_sector =extract_case_info(link,driver)
    print(docker)
    driver.quit()