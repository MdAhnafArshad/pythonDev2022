from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as web_wait
from selenium.webdriver.support import expected_conditions as EC


#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")


driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("https://perfumancebd.com/")



title_list = []

Xpath = "//*[@id='rig-adpr']/div[1]/p[1]"
xpath = "//*[@id='rig-adpr']/div[1]/p[2]"
product_img = "//*[@id='rig-adpr']/div[1]/a/img"

#for i in range(1, 127):
    
    #xPath = "//*[@id='main-content']/div[4]/div[1]/div[4]/ul/li[1]/ul/li["+str(i)+"]/div/div/div[2]/div[1]/div/span"
   
    #title_list.append(title.text)

title = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Xpath))).text
price = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath))).text
img = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, product_img)))

image = img.get_attribute('src')
    
print("title:", title)
print("image:", image)
print("price:", price)





time.sleep(100)

driver.quit()
