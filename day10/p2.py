import pandas as pd
score = {"sai":34, "pratap":45, "challa":78}
series = pd.Series(score, index=["sai", "pratap"])
print(series)
print(series['sai'])
