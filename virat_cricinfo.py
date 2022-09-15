import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
os.environ['PATH'] += r"C:\Users\hartiwar\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome("C:\\Users\\hartiwar\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.espncricinfo.com/player/virat-kohli-253802/bowling-batting-stats")
#<span class="ds-text-tight-m ds-font-bold ds-flex ds-justify-center ds-items-center ds-cursor-pointer ds-flex-1 ds-text-raw-white ds-shadow-inner-border ds-px-2">Stats</span>
data = driver.find_element(By.LINK_TEXT,value="year 2022")
time.sleep(10)
data.click()

#innis_data = driver.find_element(By.XPATH,value='/html/body/div[3]/div/div[1]/div[3]/table[3]/tbody[2]/tr/td[3]')
#<span class="player-match-link">year 2022</span>
t20_2022 = driver.find_element(By.LINK_TEXT,value="T20Is (2001 - 2022)")
time.sleep(10)
t20_2022.click()