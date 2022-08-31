from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
time.sleep(5)

# ********** LOG IN *************

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys('email')
password.send_keys('password')
# time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

count = 0

# ***************** ADD CONTACTS ***********************
for i in range(100):
    i += 1
    driver.get(
        f"https://www.linkedin.com/search/results/people/?keywords=hr&origin=SWITCH_SEARCH_VERTICAL&page={i}&sid=J6B")
    time.sleep(2)
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        # time.sleep(2)
        send = driver.find_element(
            By.XPATH, "//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        count += 1
        close = driver.find_element(
            By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        # time.sleep(2)
        print(count)
