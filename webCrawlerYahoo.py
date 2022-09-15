import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import logger as logger
class StockExtractor:
    
    def __init__(self,chromedrive_path="..//chromedriver_win32//chromedriver.exe"):
        raw_chrome_path = r'{}'.format(chromedrive_path)
        os.environ['PATH'] += raw_chrome_path
        self.driver = webdriver.Chrome(raw_chrome_path)
        self.stock_list=[]
    def create_website_connection(self,web_url):
        self.driver.get(web_url)
        self.driver.implicitly_wait(60)
    
    def fetch_data(self,days):
        historic = self.driver.find_element(By.LINK_TEXT,value="Historical Data")
        historic.click()
        dayindex=1
        xpath='//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{}]/td[2]'
        while(dayindex<=days):
            x_path=xpath.format(dayindex)
            print(xpath)
            stock_value = self.driver.find_element(By.XPATH,value=x_path)
            self.stock_list.append(float(stock_value.text.replace(",","")))
            dayindex+=1
        return self.stock_list
    def clear_driver_data(self):
        self.driver.close()
if __name__ == "__main__":
    scrapper = StockExtractor(r"C:\Users\hartiwar\Downloads\Dor\stockCrawler\chromedriver_win32\chromedriver.exe")
    scrapper.create_website_connection("https://finance.yahoo.com/quote/TATASTEEL.NS?p=TATASTEEL.NS&.tsrc=fin-srch")
    stock_data = scrapper.fetch_data(7)
    print(stock_data)
    scrapper.clear_driver_data()
    
    time.sleep(60)
    scrapper1 = StockExtractor(r"C:\Users\hartiwar\Downloads\Dor\stockCrawler\chromedriver_win32\chromedriver.exe")
    scrapper1.create_website_connection("https://finance.yahoo.com/quote/JINDALSTEL.NS?p=JINDALSTEL.NS&.tsrc=fin-srch")
    stock_data1 = scrapper1.fetch_data('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{}]/td[2]',7)
    print(stock_data1)
    scrapper.clear_driver_data()