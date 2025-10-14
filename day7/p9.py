"""
1. create a folder day8 under "pythontraining" if does not exist
2. change to day8
3. create a file file1.txt in day8
4. list all files in day8
5. rename file1.txt to file2.txt
6. list the files again in day8
7. remove file2.txt
8. list the files in "pythontraining"
9. remove day8 folder
10. list the files in "pythontraining"
"""

import os

# 1. Create day8 folder
os.chdir("..")  # Go to pythontraining
if not os.path.exists("day8"):
    os.mkdir("day8")

# 2. Change to day8
os.chdir("day8")

# 3. Create file1.txt
open("file1.txt", "w").close()

# 4. List all files in day8
print("Day8 files:", os.listdir())

# 5. Rename file1.txt to file2.txt
os.rename("file1.txt", "file2.txt")

# 6. List files again in day8
print("Day8 files after rename:", os.listdir())

# 7. Remove file2.txt
os.remove("file2.txt")

# 8. List files in pythontraining
os.chdir("..")
print("Pythontraining files:", os.listdir())

# 9. Remove day8 folder
os.rmdir("day8")

# 10. List files in pythontraining again
print("Final files:", os.listdir())


from datetime import datetime
import random