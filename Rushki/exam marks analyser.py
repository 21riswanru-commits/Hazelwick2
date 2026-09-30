count=0
high=0
total=0
marks=int(input("Enter a mark or -1 to finish:"))
high = marks
low = marks
while marks!=-1:
    if marks>=0 and marks<=100:
        count=count+1
        if marks>high:
            high=marks
        if marks<low:
            low=marks

        total=total+marks
        marks=int(input("Enter a mark or -1 to finish:"))
        
    else:
        print("Invalid")
        marks=int(input("Enter a mark or -1 to finish:"))
print("marks entered:",count)
print("Average:",total/count)
print("highest:",high)
print("lowest:",low)