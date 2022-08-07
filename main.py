import cycleBot as cb
import secrets, sys
import time
from datetime import date
import datetime
from handleInput import retrieveClasses, addToSchedule, FindEarliestRegDate, validateBike, validateTime, validateDate

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

    print('Entered data: \n',
          'Date to initialize registration:',EarliestDate,
          '\n Date of class:',ClassDate,
          '\n Class Time:',ClassTime,
          '\n Bike number:',BikeNumber)

elif (action == 'test'):
    upcomingClasses = retrieveClasses()
    for index in upcomingClasses.index:
      RegistrationDate = upcomingClasses['RegDate'][index]
      print(RegistrationDate, 'type:', type(RegistrationDate))
      ClassDate = upcomingClasses['ClassDate'][index]
      print(ClassDate, 'type:', type(ClassDate))
      ClassTime = upcomingClasses['ClassTime'][index]
      print(ClassTime, 'type:', type(ClassTime))
      BikeNum = upcomingClasses['BikeNumber'][index]
      print(BikeNum, 'type:', type(BikeNum))
    

elif (action == 'useBot'):
    credentials = secrets.get_credentials()
    upcomingClasses = retrieveClasses()
    print(upcomingClasses)
    print('creating bot...')
    bot = cb.cycleBot(credentials['email'], credentials['password'])
    '''Handle the bot functions
      login in for classes
      then try to register for classes'''
    print('logging in...')
    bot.login()
    upcomingClasses = retrieveClasses()

    exit(0)
else:
    print('please enter a valid argument')
