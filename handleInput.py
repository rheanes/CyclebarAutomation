from datetime import *
import csv
import pandas as pd
from os.path import exists


def validateDate(date_text):
    try:
        datetime.strptime(date_text, '%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be MM-DD")




def validateBike(bikenum):
    if bikenum <= 0:
        raise Exception("Sorry, bike number must be positive")
    if bikenum > 50:
        raise Exception("Sorry, bike number must not excede 50")


def FindEarliestRegDate(ClassDate):
    """Remove 8 days from this date to get the earliest registration date"""
    my_date = datetime.strptime(ClassDate, "%Y-%m-%d")
    eight_days_ago = my_date - timedelta(7)
    NewString = eight_days_ago.strftime("%Y-%m-%d")
    return NewString


def addToSchedule(payload):
    '''
  takes in payload of structure
  payload = {
      "RegDate": EarliestDate,
      "ClassDate":ClassDate,
      "ClassTime":ClassTime,
      "BikeNumber": BikeNumber
    }
  '''
    headers = ['RegDate', 'ClassDate', 'ClassTime', 'BikeNumber']
    if (exists('./schedule.csv')):
        with open('schedule.csv', 'a') as file:
            dict_object = csv.DictWriter(file, headers)
            dict_object.writerow(payload)
    else:
        with open('schedule.csv', 'w+') as file:
            dict_object = csv.DictWriter(file, headers)
            dict_object.writeheader()
            dict_object.writerow(payload)


def retrieveClasses():
    '''Get the database of all dates
    remove all previous dates
    get all dates that 
  '''
    print('Getting Schedule...')
    data = pd.read_csv('schedule.csv')
    data['ClassDate'] = pd.to_datetime(data['ClassDate'])
    data['RegDate'] = pd.to_datetime(data['RegDate'])
    sortedData = data.sort_values(by='RegDate', ascending=True)
    ##print(sortedData)
    NoOldDates = RemoveOldDates(sortedData)
    attemptToRegister = CanRegisterCurrently(NoOldDates)
    #print(attemptToRegister)
  
    return attemptToRegister


def RemoveOldDates(data):
    '''
    takes in a dataframe
    compares the class-date to the current date
    if the date has passed, remove from the datafframe and the schedule.csv
  '''
    print('Removing old classes...')
    today = pd.to_datetime('today').floor('D')
    #print(today)
    filtered_data = data[data["ClassDate"] >= today]
    return filtered_data


def CanRegisterCurrently(data):
    '''Takes in a pandas datraframe,
    returns classes the bot should try and register for
    df has col's 
    RegDate ClassDate ClassTime BikeNumber
  '''
    print('Removing unavialble classes...')
    today = pd.to_datetime('today').floor('D')
    filtered_data = data[data["RegDate"] <= today]
    return filtered_data


def displayData(EarliestDate, ClassDate, ClassTime, BikeNumber):
  print('Entered data: \n',
          'Date to initialize registration:',EarliestDate,
          '\n Date of class:',ClassDate,
          '\n Class Time:',ClassTime,
          '\n Bike number:',BikeNumber)