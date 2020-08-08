from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver_win32/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://flipkart.com/")

try:

    #when page gets opened, a login window is opened, click on cross mark
    cross = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div"))
    )
    btn = cross.find_elements_by_tag_name("button")
    btn[0].click()
	
	#find the search bar and type the product you need to search , in this case mobile and press enter
    search = driver.find_element_by_name("q")
    search.send_keys("mobile")
    search.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    #on the select option, filter minimum price to 7000
    selectoption = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select")
    selectoption.click()
    time.sleep(5)
    s = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select/option[4]')
    s.click()
    time.sleep(5)
    
	#click on flipkart assured 
    t = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[3]/div[1]/label')
    t.click()
    
    product_details = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]'))
    )
    
    #get the details of all the products
    product_list=[i for i in product_details.text.split("Add to Compare")]
    print(product_list)
    print(len(product_list))
    
except:
    driver.quit()


#time.sleep(5)
driver.quit()
