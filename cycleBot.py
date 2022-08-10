from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver

class cycleBot:
  def __init__(self, email, password):
    """Constructor, takes in cyclebar email and password"""
    self.email = email
    self.password = password
    self.bot = get_driver()


  def login(self):
    """Navigate to login page sleep, then enter email and password and submit"""
    bot = self.bot
    bot.get(
          "https://members.cyclebar.com/auth/login?location_id=cyclebar-dunwoody"
      )
    time.sleep(2)
    email = bot.find_element(by="id", value="form-input-email")
    email.send_keys(self.email)
    time.sleep(3)
    password = bot.find_element(by="id", value="form-input-password")
    password.send_keys(self.password)
    time.sleep(1)
    password.send_keys(Keys.RETURN)
    if (self.getCurrentUrl() ==
              'https://members.cyclebar.com/covid-waiver/cyclebar-dunwoody'):
          acceptCovidPolicy(bot)
    elif(self.getCurrentUrl() == 'https://members.cyclebar.com/'):
      print('Login Scuessful')
    else:
      print('Login Failed')
      
  def getCurrentUrl(self):
    print(self.bot.current_url)
    return self.bot.current_url


  def ReserveUrl(self, Url, ClassTime):
    time.sleep(5)
    print('url from inside attemptReserve', Url)
    print("Target Class time:", ClassTime)
    bot = self.bot
    bot.get(Url)
    #find all the table rows
    rows = bot.find_elements(By.XPATH, "//*[@id='root']/div[2]/div[4]/div[3]/table/tbody/tr")
    #for each row in rows, pull out the time and the button
    for r in rows:
      tds = r.find_elements(By.TAG_NAME, "td")
      if(len(tds)> 2):
        startTime = tds[1]
      else:
        continue

      print(startTime.text)

      
    return
  
  


def acceptCovidPolicy(bot):
    time.sleep(3)
    elements = bot.find_elements(By.TAG_NAME, 'button')
    for e in elements:
        e.click()
  
  
