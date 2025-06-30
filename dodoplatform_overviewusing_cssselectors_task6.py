from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)


driver.get("https://dodo.quantumnique.tech/login")

username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
username.send_keys("2025006")

password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
password.send_keys("Student@123")

submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_button.click()
print("Login submitted")

wait.until(EC.url_changes("https://dodo.quantumnique.tech/login"))
print("Redirected after login")

menu_links = {
    "ASSESSMENTS": "assessments",
    "COURSES": "courses",
    "CODE-COMPILER": "code-compiler",
    "PRACTICE": "practice",
    "LSRW": "lsrw",
    "BLOG": "blog",
    "DASHBOARD": "dashboard"
}

for link_text, expected_url in menu_links.items():
    try:
        menu_link = driver.find_element(By.LINK_TEXT, link_text)
        menu_link.click()
        time.sleep(2)
        current_url = driver.current_url
        if expected_url in current_url:
            print(f"{link_text}: Opened successfully.")
        else:
            print(f"{link_text}: Did not open correctly. URL: {current_url}")
        driver.get("https://dodo.quantumnique.tech/")
    except Exception as e:
        print(f"Error while checking {link_text}: {e}")
driver.quit()