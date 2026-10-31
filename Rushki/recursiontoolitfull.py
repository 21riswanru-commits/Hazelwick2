def countdown(n):
    while n!=1:
        n=n-1
        print(n)
        if n==1:
            print("lift off!")
n=4
countdown(n)

def reverse_string(s):
    reverse=s[::-1]
    return reverse



def is_palindrome(string):
    if rev.lower()==string.lower():
        return True
    else:
        return False


def fib_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)





string=input("Enter string:")
rev=reverse_string(string)
print("Reverse:",rev)
pal=is_palindrome(string)
print("palindrome:",pal)

terms=[]
for i in range(15):
    terms.append(fib_recursive(i))
print(terms)