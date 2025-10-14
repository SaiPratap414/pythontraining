import os
import datetime
if not os.path.exists("backup"):
    os.mkdir("backup")
os.chdir("backup")
dt = datetime.datetime.now()
folder = dt.strftime("%Y%m%d_%H%M%S")
os.mkdir(folder)
os.chdir(folder)
open("file1.txt", "w").close()
os.chdir("..")
print("Backup created on:", dt.strftime("%Y-%m-%d %H:%M:%S"))