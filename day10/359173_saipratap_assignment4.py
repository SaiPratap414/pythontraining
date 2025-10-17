import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Month':['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales':[25000,27000,30000,28000,32000,35000,40000,42000,45000,48000,50000,55000]
}

#convert to dataframe
df = pd.DataFrame(data)
print(df)

#Basic statistics
mean_sales = np.mean( df['Sales'])
max_sales = np.max( df['Sales'])
min_sales = np.min( df['Sales'])
std_dev_sales = np.std( df['Sales'])

print(f"Mean Sales: ${mean_sales:,.0f}")
print(f"Max Sales: ${max_sales:,.0f}")
print(f"Min Sales: ${min_sales:,.0f}")
print(f"Standard Deviation of Sales: ${std_dev_sales:,.0f}")

#identify best and worst months
best_month = df.loc[df['Sales'].idxmax(), 'Month']
worst_month = df.loc[df['Sales'].idxmin(), 'Month']

print(f"Best Month: {best_month}")
print(f"Worst Month: {worst_month}")

plt.figure(figsize=(10,6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-',linewidth=2, color='b')
plt.title('Monthly Sales Trend - 2024', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales ($)', fontsize=14)
plt.grid(True)
plt.show()