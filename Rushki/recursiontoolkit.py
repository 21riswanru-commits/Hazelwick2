def countdown(n):
    if n==0:
        print("Lift off!")
    else:
        print(n)
        countdown(n-1)
def reverse_string(s):
    reverse= s[::-1]
    return reverse



 



n=3
countdown(n)
string=input("Enter string:")
reverse_string(string)
r=reverse_string(string)
print(r)

