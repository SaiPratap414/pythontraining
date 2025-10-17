# import pandas as pd

# df = pd.read_csv("score.csv")

# dates = ["2024-01-15", "2024-02-20", "2024-03-10"]
# df["doj"] = pd.to_datetime(dates)
# print(df)


import pandas as pd
df = pd.read_csv("score.csv")
df ["doj"] = pd.to_datetime("doj")
print(df)