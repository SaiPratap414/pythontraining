import os 
os.chdir("pythontraining/day7")
print(os.stat("p11.py"))

from datetime import datetime
st_ctime = 1760429341
print(datetime.fromtimestamp(st_ctime))