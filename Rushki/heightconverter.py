name=input("What is your name?")
height=float(input("Enter your height in cm:"))
metres=height/100
inches=height/2.54
print("Hi",name)
print("Your height is",metres,"m")
print("That is",inches,"inches")
if height<=180:
    print("Taller than 180cm:False")
else:
    print("Taller than 180cm: True ")
