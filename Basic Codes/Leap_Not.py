# Leap year or not:
year = int(input())
if (year%4==0 and year!=100) or year%400==0:
    print("Leap Year")
else :
    print("Not a Leap Year")

# (Or)
import calendar                       #Importing Calendar
if calendar.isleap(year):
    print("Leap Year")
else:
    print("Not a Leap Year")