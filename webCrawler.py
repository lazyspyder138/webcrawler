from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class WebCrawlerNSE:
    def __init__(self,url):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.chromedriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.chromedriver.maximize_window()
        self.chromedriver.get(url)
        #driver.implicitly_wait(10)
        #sleep(10)

    def fetch_data(self,start_date,end_date):
        historic_bt=self.chromedriver.find_element(By.LINK_TEXT,value="Historical Data")
        self.chromedriver.execute_script("arguments[0].click();",historic_bt)
        
        sleep(5)
        #click on calander
        start_date_argument_set = f"arguments[0].value='{start_date}'"
        s_date=self.chromedriver.find_element(By.ID,"startDate1")
        self.chromedriver.execute_script(start_date_argument_set,s_date)
        
        end_date_argument_set = f"arguments[0].value='{end_date}'"
        e_date=self.chromedriver.find_element(By.ID,"endDate1")
        self.chromedriver.execute_script(end_date_argument_set,e_date)
        
        sleep(5)
        equity_bt=self.chromedriver.find_element(By.ID,"equity-historical-Date-filter")
        self.chromedriver.execute_script("arguments[0].click()",equity_bt)
        
        #select date
        sleep(10)
        #click on dropdown
        dropdown_bt=self.chromedriver.find_element(By.XPATH,"//button[@class='multiselect dropdown-toggle btn btn-default']")
        self.chromedriver.execute_script("arguments[0].click()",dropdown_bt)
        
        sleep(5)
        #click on eq
        eq=self.chromedriver.find_element(By.XPATH,"//input[@value='EQ']")
        self.chromedriver.execute_script("arguments[0].click()",eq)
        sleep(5)
        click_filter_bt=self.chromedriver.find_element(By.XPATH,'//*[@id="equity-historical-Date-filter"]/div[3]/button')
        self.chromedriver.execute_script("arguments[0].click()",click_filter_bt)
        sleep(5)
        
        rows=1+len(self.chromedriver.find_elements(By.XPATH,'//*[@id="equityHistoricalTable"]/tbody/tr'))
        cols = len(self.chromedriver.find_elements(By.XPATH,'//*[@id="equityHistoricalTable"]/tbody/tr/td'))
        
        stats_list=[]
        for r in range(1,rows):
            date=self.chromedriver.find_element(By.XPATH,"/html/body/div[9]/div/div/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/section/div/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(1)+"]").text
            stat=self.chromedriver.find_element(By.XPATH,"/html/body/div[9]/div/div/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/section/div/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(6)+"]").text
            print(date,'       ',stat)
            # stats_list.append((stat,date))
            stats_list.append(stat)
        return stats_list
    def clear_driver_data(self):
        self.chromedriver.close()
if __name__ == "__main__":
    scrapper = WebCrawlerNSE("https://www.nseindia.com/get-quotes/equity?symbol=TATASTEEL")
    stock_data = scrapper.fetch_data("01-09-2022", "09-09-2022")
    print(stock_data)
    scrapper.clear_driver_data()
    
    sleep(60)
    scrapper1 = WebCrawlerNSE("https://www.nseindia.com/get-quotes/equity?symbol=JINDALSTEL")
    stock_data1 = scrapper1.fetch_data("01-09-2022", "09-09-2022")
    
    print(stock_data1)
    scrapper1.clear_driver_data()
#crawler = WebCrawlerNSE("https://www.nseindia.com/get-quotes/equity?symbol=TATASTEEL")
#crawler.fetch_data("01-09-2022", "09-09-2022")
