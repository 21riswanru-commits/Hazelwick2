names=[]
for i in range(8):
    n=input("Enter names:")
    names.append(n)
ind=0
flag=()
for i in range(len(names)):
    find=input("Enter a name to find:")
    if find==names[i]:
        ind=i
        flag="found"
if flag=="found":
    print(find,"is found at position",ind)

else:
    print(find,"not found")
        

