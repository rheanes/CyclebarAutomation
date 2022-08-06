import cycleBot as cb
import secrets, sys
import time
from datetime import date
import datetime
from handleInput import *

action = 'add'
todays_date = date.today()

if (action == 'login'):
    print('login action chosen')
    credentials = secrets.get_credentials()
    bot = cb.cycleBot(credentials['email'], credentials['password'])
    bot.login()
elif (action == 'add'):
    #get user input for class date and validate
    print('Desired class date in form of: MM-DD')
    ClassDate = input()
    validateDate(ClassDate)
    ClassDate = str(todays_date.year) + '-' + ClassDate
    #get user input for user time and validdate
    print('Enter class time in form of: H:MM')
    ClassTime = input()
    validateTime(ClassTime)
    print('Enter bike number:')
    BikeNumber = int(input())
    validateBike(BikeNumber)

    print(ClassDate,ClassTime,BikeNumber)
    

elif (action == 'useBot'):
    credentials = secrets.get_credentials()
    bot = cb.cycleBot(credentials['email'], credentials['password'])
