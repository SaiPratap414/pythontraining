import matplotlib.pyplot as plt
import numpy as np
x= ["Dell","Apple","HP","Lenovo"]
y=[20,15,30,35]
plt.plot(x,y, color="blue", marker ="o", linestyle="--", label="year 2025")
plt.title("sales report")
plt.xlabel("Company")
plt.ylabel("Sales in percentage")
plt.legend()
plt.plot(x,y)
plt.show()