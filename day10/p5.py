import pandas as pd
student = {"Name": ["sai", "pratap", "challa"],
           "Age": [24, 25, 26],
           "Address": ["hyd", "bang", "chen"]}
df = pd.DataFrame(student)
print(df.head(1))