import random #for p1
import time #for p1
import calendar #for p2
import datetime #for p2

#p2
def printCal():
  cal = calendar.month(1994, 10)
  print(cal)
  
def days2BDay():
  bDay = datetime.date(1994, 10, 6)
  daysTill = datetime.date.today() - lastBDay(bDay)
  print(daysTill)
def lastBDay(bDay):
  currentDate = datetime.date.today()
  thisYear = currentDate.year
  bDayThisYear = datetime.date(thisYear, bDay.month, bDay.day)
  if bDayThisYear > currentDate:
    return datetime.date(thisYear - 1, bDay.month, bDay.day)
  else:
    return bDayThisYear

def dayOfDeclaration():
  dayName = ""
  declarationDate = datetime.date(1776, 6, 4)
  
  weekDay = datetime.date.weekday(declarationDate)
  dayName = getDayName(weekDay)
  
  monthNum = int(str(declarationDate)[5:7])
  monthName = getMonthName(monthNum)
  
  day = declarationDate.day
  year = declarationDate.year
  
  print("%s %s %dth, %d" %(dayName, monthName, day, year))

def getMonthName(monthNum):
  monthList = ["January", "Feburary", "March", "April", "May", \
               "June", "July", "August", "September", "October", \
               "November", "December"]
  return monthList[monthNum]

def getDayName(weekDay):
  dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  return dayList[weekDay] 
  
  

#p1
def game():
  gameRunning = True
  numOfRolls = 1
  point = 0
  while gameRunning:
    firstRoll = int(getDieRoll())
    secondRoll = int(getDieRoll())
    dieTotal = firstRoll + secondRoll
    print("Your die rolls are %d and %d." %(firstRoll, secondRoll))
    if isWin(dieTotal, point, numOfRolls):
      print("Congradulations! You Won!")
      break
    elif isLose(dieTotal, point, numOfRolls):
      print("Sorry. You Lose.")
      break
    if numOfRolls == 1:
      point = dieTotal
    numOfRolls += 1

def isWin(dieTotal, point, numOfRolls):
  if numOfRolls == 1 and (dieTotal == 7 or dieTotal == 11):
    return True
  elif dieTotal == point:
    return True
  else:
    return False
    
def isLose(dieTotal, point, numOfRolls):
  if numOfRolls == 1 and (dieTotal == 2 or dieTotal == 3 or dieTotal == 12):
    return True
  elif numOfRolls > 1 and dieTotal == 7:
    return True
  else:
    return False

def getDieRoll():
  random.seed(time.clock())
  rn = random.random()
  sidesOfDice = 6
  
  diceRoll = ceil(rn * sidesOfDice)
  
  return(diceRoll)