def sum_digits(n):
    if n<10:
        return n
    else:
        return n%10+ sum_digits(n//10)

num=int(input("Enter num:"))
total=sum_digits(num)
print(total)