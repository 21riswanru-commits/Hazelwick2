mark=int(input("Enter the test mark(0-100):"))
if mark>=0 and mark<=100:
    if mark>=70:
        grade="A"
    elif mark>=60:
        grade="B"
    elif mark>=50:
        grade="C"
    elif mark>=40:
        grade="D"
    else:
        grade="U" 
    print("grade:",grade)
else:
    print("Error, mark must be between 0-100")
