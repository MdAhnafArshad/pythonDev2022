from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("https://www.rokomari.com/electronics?ref=nm")

title_list = []
immage_list = []

for section in range(1, 10):
    title = driver.find_element(by=By.XPATH, value= '/html/body/div[5]/div/div[1]/div[2]/section/div[2]/div/div['+str(section)+']/div/a/div[2]/p[1]').text

title_list.append(title)

print(title_list)




