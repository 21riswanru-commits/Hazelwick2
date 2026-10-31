def power(base,exponent):
    if exponent==0:
        return 1
    else:
        return base*power(base,exponent-1)

b=int(input("Enter base number:"))
e=int(input("Enter exponent:"))
print(power(b,e))
