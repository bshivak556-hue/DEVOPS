from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
try:
    driver.get(Path(__file__).with_name("program.html").resolve().as_uri())
    driver.find_element(By.ID, "increment-button").click()
    result = driver.find_element(By.ID, "output").text
    assert result == "1", f"Expected '1', got {result!r}"
    print("PASS: increment button updates output to 1")
finally:
    driver.quit()