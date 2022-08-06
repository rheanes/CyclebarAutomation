import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime as dt

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(
        "https://members.cyclebar.com/auth/login?location_id=cyclebar-dunwoody"
    )

    return driver


def login(driver, userEmail, userPassword):
    time.sleep(2)
    email = driver.find_element(by="id", value="form-input-email")
    time.sleep(3)
    password = driver.find_element(by="id", value="form-input-password")
    email.send_keys(userEmail)
    time.sleep(2)
    password.send_keys(userPassword)
    password.send_keys(Keys.RETURN)


def acceptCovidPolicy(driver):
    time.sleep(3)
    elements = driver.find_elements(By.TAG_NAME, 'button')
    for e in elements:
        e.click()


def main():
    driver = get_driver()
    email = os.environ['uname']
    password = os.environ['pword']
  
    login(driver, email, password)
    if (driver.current_url ==
            'https://members.cyclebar.com/covid-waiver/cyclebar-dunwoody'):
        acceptCovidPolicy(driver)

    time.sleep(6)
    driver.get('https://members.cyclebar.com/book/cyclebar-dunwoody')
    time.sleep(20)


main()
