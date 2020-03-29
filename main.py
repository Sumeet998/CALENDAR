#firstly import the module calendar

import calendar

#specify the year from the user
yy=int(input("enter the year:"))

#specify the month number from the user
mm=int(input("enter the month number:"))

#display the desired month to the user
print(calendar.month(yy,mm))
