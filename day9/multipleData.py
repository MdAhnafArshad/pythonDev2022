from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("https://www.rokomari.com/product/category/2236/calculator")

title_list = []
img_list = []

for section in range(1,6):
        title = driver.find_element(by=By.XPATH, value= '/html/body/div[5]/div/div[1]/div[2]/section/div[2]/div/div['+str(section)+']/div/a/div[2]/p[1]').text
        title_list.append(title)
        
        img = driver.find_element(by=By.XPATH, value= '/html/body/div[5]/div/div[1]/div[2]/section/div[2]/div/div['+str(section)+']/div/a/div[1]/img').get_attribute('src')
        img_list.append(img)
        



print(title_list)
print(img_list)


time.sleep(60)
quit()