from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome()
driver.get("https://www.python.org")
search_box=driver.find_element(By.NAME,"q")
query = "pycon"
for char in query:
    search_box.send_keys(char)
    time.sleep(0.3) 
search_box.send_keys(Keys.RETURN)
time.sleep(2)

if "No results found." not in driver.page_source:
    print("searching result for  pycon")
    
else:
    print("no result found")
    
driver.quit()