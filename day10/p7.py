import pandas as pd
df = pd.read_csv("score.csv")
df.fillna(5, inplace=True)
df.loc[df['Subject'] == "Python", 'Score'] = 5
print(df)   