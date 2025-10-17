import pandas as pd
score = {"sai":[34], "pratap":[45], "challa":[78]}
df = pd.DataFrame(score, index=["python", "java", "c++"])
df.to_csv("score.csv", index=True)
# print(df.loc["python"])
# print(df['sai'])