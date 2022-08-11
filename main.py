import os
import cycleBot as cb
import secrets, sys
import time
from datetime import date
import datetime
from handleInput import retrieveClasses, addToSchedule, FindEarliestRegDate, validateBike, validateDate

if (len(sys.argv) > 1):
    action = sys.argv[1]
else:
    action = 'useBot'

todays_date = date.today()

if (action == 'add'):
    #get user input for class date and validate
    print('Desired class date in form of: MM-DD')
    ClassDate = input()
    validateDate(ClassDate)
    ClassDate = str(todays_date.year) + '-' + ClassDate
    EarliestDate = FindEarliestRegDate(ClassDate)
    #get user input for user time and validdate
    print('Enter class time in form of: H:MMam/pm, including am or pm')
    ClassTime = input()
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
      ClassDate = upcomingClasses['ClassDate'][index]
      classDateString = ClassDate.strftime('%Y-%m-%d')
      ClassTime = upcomingClasses['ClassTime'][index]
      url = f"https://members.cyclebar.com/book/cyclebar-dunwoody?date={classDateString}"
      print(url)
    

elif (action == 'useBot'):
    credentials = secrets.get_credentials()
    my_user = os.environ['uname']
    my_pword = os.environ['pword']
    upcomingClasses = retrieveClasses()
    print('creating bot...')
    #bot = cb.cycleBot(credentials['email'], credentials['password'])
    bot = cb.cycleBot(my_user, my_pword)
    '''Handle the bot functions
      login in for classes
      then try to register for classes'''
    print('logging in...')
    bot.login()
    upcomingClasses = retrieveClasses()
    for index in upcomingClasses.index:
      ClassDate = upcomingClasses['ClassDate'][index]
      classDateString = ClassDate.strftime('%Y-%m-%d')
      ClassTime = upcomingClasses['ClassTime'][index]
      BikeNum = upcomingClasses['BikeNumber'][index]
      RegistrationDate = upcomingClasses['RegDate'][index]
      url = f"https://members.cyclebar.com/book/cyclebar-dunwoody?date={classDateString}"
      classFound = bot.ReserveUrl(url, ClassTime)
      if(classFound):
        bot.selectBike(BikeNum)
      

    

    exit(0)
else:
    print('please enter a valid argument')
