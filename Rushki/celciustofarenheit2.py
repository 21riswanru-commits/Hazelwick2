def ctof(celcius):
    farn=celcius*(9/5)+32
    return farn

def pct(start,end,step):
    print("Celcius          farenheit")
    for c in range(start,end+1,step):
        print(f"{c:<17}{ctof(c)}")

cel=float(input("Enter temp in celcius:"))
far=ctof(cel)
print(far)
pct(0,50,10)