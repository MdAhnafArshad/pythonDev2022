from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.facebook.com/?stype=lo&jlou=AfeJpXAZRHoa98BIvN0sguICAkRqqv8mLPZIWvkzk1FXIHy0y6uz1q3zk3XvaMiyz_KIoFHgNzlngxaev_uULNn0Ni10MfrWitqdt7TE6habJQ&smuh=16442&lh=Ac_xLRmmJxVtGeAGI2s')


#Get this element
Email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
login = driver.find_element(by=By.CSS_SELECTOR, value='[name="login"]')

#send this value into the element
Email.send_keys('gopro@gmail.com')
password.send_keys('gopRorolemap')
login.submit()


time.sleep(600)
quit()

