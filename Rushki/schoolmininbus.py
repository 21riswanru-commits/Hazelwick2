capacity=16
num=int(input("How many students are going on the trip?"))
full=num//capacity
remainder=num%capacity
print(f"full minibuses:{full}")
print(f"Students left over:{remainder}")
