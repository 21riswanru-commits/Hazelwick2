mark=int()
count=0
total=0
high=0
low=100
while mark!=-1:
    mark=int(input("Enter a mark(or -1 to finish)"))
    if mark<0 or mark>100:
        print("Invalid mark must be between 0 and 100")
    else:
        count=count+1
        total=total+mark
        if mark>high:
            high=mark
        if mark<low:
            low=mark
print("Marks entered:",count)
print("Average:",float(total/count))
print("Highest:",high)
print("Lowest:",low)      