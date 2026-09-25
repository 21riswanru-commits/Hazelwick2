number=int(input("Enter a 3-digit number:"))
hundreds=number//100
remaining=number%100
tens=remaining//10
remaining2=remaining%10
units=remaining2//1
sum=hundreds+tens+units
reversed=#reverse code
print("Hundreds:",hundreds)
print("Tens:",tens)
print("Units",units)
print("Sum of digits:",sum)
print("Reversed:",reversed)
if number%2==0:
    print("Even number: True")
else:
    print("Even number: False")

