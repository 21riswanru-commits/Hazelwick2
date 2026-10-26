timetable=int(input("Enter your timetable(1-12)"))
while timetable<1 or timetable>12:
    print("Invalid must be between (1-12)")
    timetable=int(input("Enter your timetable(1-12)"))
  
for num in range(1,13):
    print(num,"x",timetable,"=",num*timetable)


