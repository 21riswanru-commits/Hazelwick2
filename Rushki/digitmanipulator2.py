num=int(input("Enter a three digit number:"))
hundreds=num//100
remainder=num%100
tens=remainder//10
ones=remainder%10
sum=hundreds+tens+ones
reversed=str(num)[::-1]
print("hundreds:",hundreds)
print("tens:",tens)
print("Units:",ones)
print("Sum of digits:",sum)
print("Reversed:",reversed)
if num%2==0:
    print("Even number:True")
else:
    print("Even number:False")