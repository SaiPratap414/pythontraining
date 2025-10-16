import matplotlib.pyplot as plt
import numpy as np

x = ["Dell","Apple","HP","Lenovo"]
y = [20,15,30,35]

plt.scatter(x, y, color="blue", s=100, marker="x", label="year 2025")
plt.title("Sales Report")
plt.xlabel("Company")
plt.ylabel("Sales in percentage")
plt.legend()
plt.show()