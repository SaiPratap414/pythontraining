import pandas as pd
df = pd.read_csv("score.csv")
# print(df)

pd.options.display.max_rows = 1
pd.options.display.max_columns = 1
print(df)
# print(pd.options.display.max_rows)