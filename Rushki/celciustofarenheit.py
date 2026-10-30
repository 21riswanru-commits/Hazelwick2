def celcius_to_farenheit(celcius):
    farn= celcius*(9/5)+32
    return farn 

def print_conversion_table(start,end,step):
    print("celcius          farenheit")
    for c in range(start,end+1,step):
        print(f"{c:<17}{celcius_to_farenheit(c)}")

c=float(input("Enter celcius value to convert:"))
f=celcius_to_farenheit(c)
print(f)
print_conversion_table(0,50,10)