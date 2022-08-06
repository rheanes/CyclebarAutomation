from datetime import *


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