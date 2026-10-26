import random
num=random.randint(1,100)
guess=int()
count=1
while guess!=num:
    guess=int(input("Enter your guess(1-100):"))
    count=count+1
    if guess>num:
        print("Too high!")
    elif guess<num:
        print("Too low!")
    else:
        print("Correct!You took",count,"guesses")
