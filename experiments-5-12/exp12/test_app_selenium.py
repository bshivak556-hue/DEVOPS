import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
try:
    driver.get(os.getenv("APP_URL", "http://127.0.0.1:8080"))
    assert driver.title == "My Containerized Application", driver.title
    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")
    driver.find_element(By.NAME, "submit").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "Form submitted successfully!", result
    print("PASS: home page and form submission")
finally:
    driver.quit()