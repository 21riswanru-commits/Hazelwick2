age=int(input("Enter your age:"))
if age<0:
    print("Error")
else:
    if age<12 and age>0:
        price=5.00
    elif age>=12 and age<=17:
        price=7.00
    elif age>=18 and age<=64:
        card=input("Do you have a student card (Y/N):")
        if card=="Y":
            price=8.00
        else:
            price=10.00
    elif age>=65:
        price=6.00
    print("ticket price:",price)