from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os
import random


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
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
        time.sleep(getRandom(1,3))
        email = bot.find_element(by="id", value="form-input-email")
        email.send_keys(self.email)
        time.sleep(getRandom(2,4))
        password = bot.find_element(by="id", value="form-input-password")
        password.send_keys(self.password)
        time.sleep(getRandom(2,4))
        password.send_keys(Keys.RETURN)
        if (self.getCurrentUrl() ==
                'https://members.cyclebar.com/covid-waiver/cyclebar-dunwoody'):
            acceptCovidPolicy(bot)
        elif (self.getCurrentUrl() == 'https://members.cyclebar.com/'):
            print('Login Scuessful')
        else:
            print('Login Failed')

    def getCurrentUrl(self):
        print(self.bot.current_url)
        return self.bot.current_url

    def ReserveUrl(self, Url, ClassTime):
        time.sleep(getRandom(1,3))
        bot = self.bot
        bot.get(Url)
        #find all the table rows
        rows = bot.find_elements(
            By.XPATH, "//*[@id='root']/div[2]/div[4]/div[3]/table/tbody/tr")
        #for each row in rows, pull out the time and the button
        for r in rows:
            tds = r.find_elements(By.TAG_NAME, "td")
            if (len(tds) < 2):
                continue
            startTime = tds[1].text.split('–')[0]
            if (startTime == ClassTime):
                print('bike found!!')
                button = r.find_element(By.TAG_NAME, "button")
                scrollToElement(bot, button)
                button.click()
                print(bot.current_url, '\n', Url)
                if (bot.current_url == Url):
                    print('accepting covid policy...')
                    acceptCovidPolicy(bot)
                return True
        print('target not found')
        return False

    def selectBike(self, bikeNumber):
        bikeNumb = str(bikeNumber)
        print('Bike number:', bikeNumber)
        bot = self.bot
        availableSeats = bot.find_elements(By.CLASS_NAME,
                                           "spot-seat-selectable")
        seatIsFree = False
        for seat in availableSeats:
            print(seat.text)
            if (seat.text == bikeNumb):
                seat.click()
                seatIsFree = True
                break

        if (seatIsFree):
            button = bot.find_element(
                By.XPATH,
                '//*[@id="root"]/div[2]/div/div/div/div[2]/div[3]/button')
            time.sleep(getRandom(1,3))
            print('button text:', button.text)
            button.click()
            return True
        else:
            print('Bike is not available!')
            return False

    def confirmBooking(self):
        # This should only be done at midnight.
        return


def scrollToElement(bot, Element):
    bot.execute_script("arguments[0].scrollIntoView()", Element)
    time.sleep(getRandom(1,3))


def acceptCovidPolicy(bot):
    time.sleep(getRandom(1,3))
    element = bot.find_element(By.TAG_NAME, 'button')
    scrollToElement(bot, element)
    element.click()


def getRandom(low, high):
  rand = random.randint(low, high)
  print('Counting to: ', rand)
  return rand
