from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as web_wait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome( service =Service(ChromeDriverManager().install()))
driver.get('https://perfumancebd.com/')

#xpath = '//*[@id="rig-adpr"]/div[1]/p[1]'
#title = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
#print(title.text)

listOfData = []
n = 9
for i in range(n):
    xpath = '//*[@id="rig-adpr"]/div["+str(i)+"]/p[1]' 
    title = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    listOfData.append(title.text)

print("value of list", listOfData)

