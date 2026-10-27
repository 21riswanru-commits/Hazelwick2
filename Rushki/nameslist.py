names=[]
for n in range(8):
    name=input("Enter the names:")
    names.append(name)
found=False
search=input("Enter the name to be searched for:")
for s in range(len(names)):
    if names[s]==search:
        found=True
        print(names[s],"Found at position",s+1)
if found==False:
    print(search,"not found")
        