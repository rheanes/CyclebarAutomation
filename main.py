import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver.get("https://members.cyclebar.com/auth/login?location_id=cyclebar-dunwoody")
    return driver

def login(driver):
  time.sleep(2)
  email = driver.find_element(by="id", value="form-input-email")
  time.sleep(3)
  password = driver.find_element(by="id", value="form-input-password")
  email.send_keys("rhilleanes@gmail.com")
  password.send_keys("seleniumAutomation1")
  password.send_keys(Keys.RETURN)

def main():
  driver = get_driver()
  login(driver)
  
  time.sleep(3)
  if(driver.current_url == 'https://members.cyclebar.com/covid-waiver/cyclebar-dunwoody'):
    driver.find_element(by='xpath', value='/html/body/div[2]/div[2]/div/button').click()
  time.sleep(6)
  driver.find_element(by='xpath', value='/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/small/a').click()
  time.sleep(20)

main()