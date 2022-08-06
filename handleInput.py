from datetime import *
import csv
import pandas as pd
from os.path import exists

def validateDate(date_text):
  try:
    datetime.strptime(date_text, '%m-%d')
  except ValueError:
    raise ValueError("Incorrect data format, should be MM-DD")

def validateTime(time_text):
  try:
    datetime.strptime(time_text, '%H:%M')
  except ValueError:
    raise ValueError("Incorrect data format, should be MM-DD")

def validateBike(bikenum):
  if bikenum<=0:
    raise Exception("Sorry, bike number must be positive")
  if bikenum>50:
    raise Exception("Sorry, bike number must not excede 50")


def FindEarliestRegDate(ClassDate):
  """Remove 8 days from this date to get the earliest registration date"""
  my_date = datetime.strptime(ClassDate, "%Y-%m-%d")
  eight_days_ago = my_date - timedelta(8)
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
  headers = ['RegDate','ClassDate','ClassTime','BikeNumber']
  if(exists('./schedule.csv')):
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
  data = pd.read_csv('schedule.csv')
  NoOldDates = RemoveOldDates(data)
  #TryRegisterFor = CanRegisterCurrently(RemoveOldDates)
  return data

def RemoveOldDates(data):
  '''
    takes in a dataframe
    compares the class-date to the current date
    if the date has passed, remove from the datafframe and the schedule.csv
  '''
  today = pd.to_datetime('today').floor('D')
  data['ClassDate'] = pd.to_datetime(data['ClassDate'])
  filtered_data = data[data["ClassDate"]>= today]
  return filtered_data

def CanRegisterCurrently(data):
  '''Takes in a pandas datraframe,
    returns classes the bot should try and register for
    df has col's 
    RegDate ClassDate ClassTime BikeNumber
  '''
  for row in data:
    print(row)
  return