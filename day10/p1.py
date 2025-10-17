import pandas as pd
score =[34,45,78]
series = pd.Series(score, index=['sai', 'pratap', 'pooja'])
print(series)
print(series['sai'])
print(series[1])