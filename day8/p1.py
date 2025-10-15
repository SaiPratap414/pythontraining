# os.chdir("day8")
f=open("file1.txt","a" )

while True:
    n = input("Enter name: ")
    f.write(n)
    ch = input("contnue? (y/n): ")
    if ch!='y':
        break
f.close()