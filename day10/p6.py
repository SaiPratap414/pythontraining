# import pandas as pd
# df = pd.read_csv("score.csv")
# print(df)
# new_df = df.dropna()
# print(new_df)

import pandas as pd
# Read and reshape data
df = pd.read_csv("score.csv", index_col=0)
df_melted = df.reset_index().melt(id_vars='index', var_name='Student', value_name='Score')
df_melted.rename(columns={'index': 'Subject'}, inplace=True)

print("Reshaped data:")
print(df_melted)

# Now you can use Subject column
df_melted.fillna(5, inplace=True)
df_melted.loc[df_melted['Subject'] == "python", 'Score'] = 100

print("\nAfter updating python scores:")
print(df_melted)