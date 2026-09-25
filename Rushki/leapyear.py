#calculate if its a leap year or not
year=int(input("Enter a year:"))
if year//4==0 and year//100!=0:
    print(year,"is a leap year")
elif year//4!=0 and year//100!=0  or year//400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


#number of days in month depending on the month and whether it is or isn't a leap year
month=int(input("Enter a month number (1-12):"))
if month<1 or month>12:
    print("error")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Month", month, "of", year, "has 29 days")
    else:
        print("Month", month, "of", year, "has 28 days")
if month==4 or month==6 or month==9 or month==11:
    print("Month",month,"of",year,"has 30 days:")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("Month",month,"of",year,"has 31 days:")
