# os.chdir("day8")
f=open("file1.txt","a" )

while True:
    n = input("Enter name: ")
    f.write(n)
    ch = input("contnue? (y/n): ")
    if ch!='y':
        break
f.close()
with open("file1.txt") as f:
    for line in f:
        print(line.strip())
        
# file = open("file1.txt", "r")
# data = f.read()
# print("Data in file1.txt:")
# file.close()