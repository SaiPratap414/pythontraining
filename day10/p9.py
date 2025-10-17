import pandas as pd
df = pd.read_csv("score.csv")

for r in df.index:
    if df.loc[r, 'sai'] > 30:
        # df.loc[r, 'sai'] = 95
        df.drop(r, inplace=True)
print(df.to_string())
