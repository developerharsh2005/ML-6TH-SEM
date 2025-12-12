import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 6, 10, 13, 11])

b0 = 3
b1 = 2
alpha = 0.1
iterations = 5
n = len(x)


b0_list = [b0]
b1_list = [b1]


for i in range(iterations):
    y_pred = b0 + b1 * x
    e = y_pred - y

    sum_e = np.sum(e)
    sum_ex = np.sum(e * x)

    
    b0 = b0 - alpha * (sum_e / n)
    b1 = b1 - alpha * (sum_ex / n)

    b0_list.append(b0)
    b1_list.append(b1)

    print(f"Iteration {i+1}:  b0 = {b0:.4f}, b1 = {b1:.4f}")



plt.figure(figsize=(8,6))
plt.scatter(x, y, color='red', label="Actual data", s=60)


for i in range(len(b0_list)):
    y_line = b0_list[i] + b1_list[i] * x
    plt.plot(x, y_line, label=f"Iter {i}")

plt.title("Gradient Descent Regression Updates")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, [0]*len(x), y, color='red', s=60, label="Actual Data")


for i in range(len(b0_list)):
    y_pred_line = b0_list[i] + b1_list[i] * x
    ax.plot(x, [i]*len(x), y_pred_line, label=f"Iter {i}")

ax.set_xlabel("x")
ax.set_ylabel("Iteration")
ax.set_zlabel("y / y_pred")
ax.set_title("3D Gradient Descent Line Updates")
ax.legend()

plt.show()
