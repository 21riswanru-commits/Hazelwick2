temperature=[]
for i in range(5):
    temp=float(input("Enter a temperature:"))
    temperature.append(temp)

total=0
highest=temperature[0]
for t in temperature:
    total=total+t
    if t > highest:
        highest=t
average=total/len(temperature)
count=0
for te in temperature:
    if te>average:
        count=count+1
print("temperatures:",temperature)
print("average:",average)
print("highest:",highest)
print("days above average:",count)