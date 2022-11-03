from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.amazon.com/dp/B0B4GC9TJT?ref_=nav_em__k_ods_eink_kke_0_2_3_2')


#variable diclearation




Title = driver.find_element(by=By.XPATH, value='//*[@id="productTitle"]').text
img = driver.find_element(by=By.XPATH, value='//*[@id="landingImage"]').get_attribute('src')
rating = driver.find_element(by=By.XPATH, value='//*[@id="acrPopover"]/span[1]/a/i[1]/span').get_attribute('innerHTMl')

list_of_Data = [Title, img, rating]


print(list_of_Data)







