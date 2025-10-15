import os
os.chdir("day8/quiz")
file = open("Questions1.txt", "r")
for line in file:
    print(line.strip())
file.close()