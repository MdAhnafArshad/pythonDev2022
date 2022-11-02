from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


print(driver.get('https://www.amazon.com/Beats-Studio3-Wireless-Over%E2%80%91Ear-Headphones/dp/B085296FLT/'))


#variable diclearation
title = driver.find_element(by=By.XPATH, value='//*[@id="title"]')
current_price = driver.find_element(by=By.XPATH, value='//*[@id="compare"]/table/tbody/tr[2]/td[4]/span/span')

product_data = {
    'title': title.text,
    'current_price': current_price.get_attribute('innerHTML')
}

print(product_data)