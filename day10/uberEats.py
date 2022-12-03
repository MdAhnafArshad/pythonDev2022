from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as web_wait
from selenium.webdriver.support import expected_conditions as EC


#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")


driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("https://www.ubereats.com/store/birds-burger-bar/wbbxTPolQFuurGeGNCRaaQ?diningMode=DELIVERY&nt=1&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzNTIlMkMlMjJsb25naXR1ZGUlMjIlM0EtNzQuMDA2ODg1JTdE")



title_list = []


for i in range(1, 6):

    xPath = "//*[@id='main-content']/div[4]/div[1]/div[4]/ul/li[1]/ul/li["+str(i)+"]/div/div/div[2]/div[1]/div/span"
    title = web_wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xPath)))
    title_list.append(title.text)


print(title_list)




time.sleep(100)

driver.quit()
