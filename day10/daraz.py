from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as web_wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get('https://www.daraz.com.bd/men-muslim-wear/?spm=a2a0e.home.cate_4.4.573f12f7aiGQf3')


product_title_list= []
title = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xPath)))

for i in range(1, 40):
    xPath = "//*[@id='root']/div/div[3]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a"
    product_title_list.append(title.text)

print(product_title_list)
