one="add an item"
two="remove an item"
three="view the list"
four="count items"
five="quit"
print("1.",one)
print("2.",two)
print("3.",three)
print("4.",four)
print("5.",five)

list=[]
count=0
option=int()
while option!=5:
    if option>=1 or option<=5:
        option=int(input("Choose an option:"))
        if option==1:
            add=input("Item to add:")
            list.append(add)
            print(add,"added")
            if add in list:
                list.append(add)
                print(add,"already in list")
        elif option==2:
            remove=input("Item to remove:")
            if remove in list:
                list.remove(remove)
                print(remove,"removed")
            else:
                    print(remove,"is not in the list")
        elif option==3:
            if len(list)!=0:
                for l in list:
                    count=count+1
                    print(count,".",l)
            else:
                print("your list is empty")
        else:
            print("number of items:",len(list))
        
    
    

