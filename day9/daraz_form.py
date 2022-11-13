from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://member.daraz.com.bd/user/login?spm=a2a0e.home.header.d5.735212f7XoX8sX&redirect=https%3A%2F%2Fwww.daraz.com.bd%2F')


#Get this element
Email = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]/input')
password = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[2]/form/div/div[1]/div[2]/input')
login = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button')

#send this value into the element
Email.send_keys('TestValue@gmail.com')
password.send_keys('testFile')
login.submit()


time.sleep(600)
quit()

