import datetime


def validateDate(date_text):
  try:
    datetime.datetime.strptime(date_text, '%m-%d')
  except ValueError:
    raise ValueError("Incorrect data format, should be MM-DD")

def validateTime(time_text):
  try:
    datetime.datetime.strptime(time_text, '%H:%M')
  except ValueError:
    raise ValueError("Incorrect data format, should be MM-DD")

def validateBike(bikenum):
  if bikenum<=0:
    raise Exception("Sorry, bike number must be positive")
  if bikenum>50:
    raise Exception("Sorry, bike number must not excede 50")

