# os module
import os

# Change to correct directory
os.chdir("pythontraining/day7")

# List files
print(os.listdir())

# Replace file
# os.replace("temp.txt", "tmp.txt")
# print("File renamed successfully!")

open("file1.txt", "w").close()