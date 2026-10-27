temperatures=[]
count=0
for i in range(5):
    count=count+1
    temp=float(input(f"Enter temperature {count}:"))
    temperatures.append(temp)

average=sum(temperatures)/len(temperatures)

high=temperatures[0]
for h in temperatures:
    if h>high:
        high=h
d=0
for a in temperatures:
    if a>average:
        a=a
        d=d+1

print("temperatures:",temperatures)
print("Average:",average)
print("Highest:",high)
print("Days above average:",d)
       







