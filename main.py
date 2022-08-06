import cycleBot as cb
import secrets, sys
import time
from datetime import date
import datetime
from handleInput import *

if (len(sys.argv) > 1):
    action = sys.argv[1]
else:
    action = 'test'

todays_date = date.today()

if (action == 'add'):
    #get user input for class date and validate
    print('Desired class date in form of: MM-DD')
    ClassDate = input()
    validateDate(ClassDate)
    ClassDate = str(todays_date.year) + '-' + ClassDate
    EarliestDate = FindEarliestRegDate(ClassDate)
    #get user input for user time and validdate
    print('Enter class time in form of: H:MM')
    ClassTime = input()
    validateTime(ClassTime)
    print('Enter bike number:')
    BikeNumber = int(input())
    validateBike(BikeNumber)
    payload = {
        "RegDate": EarliestDate,
        "ClassDate": ClassDate,
        "ClassTime": ClassTime,
        "BikeNumber": BikeNumber
    }
    addToSchedule(payload)

    print(EarliestDate, ClassDate, ClassTime, BikeNumber)

elif (action == 'test'):
    upcomingClasses = retrieveClasses()

elif (action == 'useBot'):
    print('getting credentials...')
    credentials = secrets.get_credentials()
    print('Getting Schedule:')
    upcomingClasses = retrieveClasses()
    print(upcomingClasses)
    print('creating bot...')
    bot = cb.cycleBot(credentials['email'], credentials['password'])
    '''Handle the bot functions
      login in for classes
      then try to register for classes'''
    print('logging in...')
    bot.login()
    #for c in upcoming classes
    exit(0)
else:
    print('please enter a valid argument')
