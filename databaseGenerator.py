import pathlib
import csv 
import random

path = pathlib.Path('db/data/')

def writeToFile(filename, rows):
  
  fpath = (path / filename).with_suffix('.csv')
  with fpath.open(mode='a') as csvfile:
    writer = csv.writer(csvfile)
   
    writer.writerows(rows)

def generateRows(rowFunction): 
  rows = []
  for i in range(26, 5000): 
      rows.append(rowFunction(i))
  return rows

def activityRow(i): 
  return ["fakeactivity{num}".format(num = i)] 

def eventRow(i):
  year = random.randint(2000, 2021)
  month = random.randint(1,12)
  day = random.randint(1, 28)
  randomDate = "{}-{:02d}-{:02d}".format(year, month, day)
  randomActivity = "fakeactivity{num}".format(num = i)
  randomEvent = "Fake Event {num}".format(num = i)
  return [randomEvent, randomActivity, randomDate]

def leagueRow(i):
  return [i, "fake league{num}".format(num = i), "fake name{num}".format(num = i)]

def participatesRow(i): 
  return [i, "fakeactivity{num}".format(num = i), random.randint(200, 2000)]

def peopleRow(i): 
  return [i, "fake name{num}".format(num = i), "password1"]

  
def rankableRow(i): 
  return [i, "People", "fake name{num}".format(num = i)]

def matchRow(i): 
  year = random.randint(2000, 2021)
  month = random.randint(1,12)
  day = random.randint(1, 28)
  hour = random.randint(1, 12)
  minute = random.randint(0, 59)
  second = random.randint(0, 59)

  timestamp = "{}-{:02d}-{:02d} {}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
  return ["fakeactivity{num}".format(num = i), i, random.randint(20, 4999),  random.randint(20, 4999),  random.randint(0, 21),  random.randint(0, 21), timestamp]


writeToFile("Matches", generateRows(matchRow))