import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 6, 10, 13, 11])

# Parameters
b0 = 3
b1 = 2
alpha = 0.1
iterations = 5
n = len(x)

# For storing history for plotting
b0_list = [b0]
b1_list = [b1]

# Gradient Descent (Mean formula)
for i in range(iterations):
    y_pred = b0 + b1 * x
    e = y_pred - y

    sum_e = np.sum(e)
    sum_ex = np.sum(e * x)

    # Update using MEAN formula
    b0 = b0 - alpha * (sum_e / n)
    b1 = b1 - alpha * (sum_ex / n)

    b0_list.append(b0)
    b1_list.append(b1)

    print(f"Iteration {i+1}:  b0 = {b0:.4f}, b1 = {b1:.4f}")

# ----------------- PLOT REGRESSION LINES -----------------

plt.figure(figsize=(8,6))
plt.scatter(x, y, color='red', label="Actual data", s=60)

# Plot line after each iteration
for i in range(len(b0_list)):
    y_line = b0_list[i] + b1_list[i] * x
    plt.plot(x, y_line, label=f"Iter {i}")

plt.title("Gradient Descent Regression Updates")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
