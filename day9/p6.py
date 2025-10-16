import matplotlib.pyplot as plt
import numpy as np

x = ["Dell","Apple","HP","Lenovo"]
y = [20,15,30,35]

colors = ['red', 'blue', 'green', 'orange']

plt.pie(y, 
        labels=x, 
        autopct='%1.1f%%',     # Show percentages
        colors=colors,          # Custom colors
        startangle=90,          # Start angle
        explode=(0.1, 0, 0, 0)) # Explode first slice

plt.title("Sales Report - Pie Chart")
plt.show()