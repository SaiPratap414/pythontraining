names={}
while True:
    name = input("Enter a name:")
    names[name]=names.get(name,0)+1
    flag = input("Do you want to continue(y/n)")
    if flag!="y":
        break

print(names)