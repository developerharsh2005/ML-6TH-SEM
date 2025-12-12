import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X1 = [60, 62, 67, 70, 71, 72, 75, 78]
X2 = [22, 25, 24, 20, 15, 14, 14, 11]
Y  = [140,155,159,179,192,200,212,215]

X = np.column_stack((X1, X2))

model = LinearRegression()
model.fit(X, Y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

new = [[80, 24]]
print("Prediction for X1=80, X2=24 →", model.predict(new))

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.scatter(X1, Y, color='blue')
plt.xlabel("X1")
plt.ylabel("Y")
plt.title("X1 vs Y")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(X2, Y, color='red')
plt.xlabel("X2")
plt.ylabel("Y")
plt.title("X2 vs Y")
plt.grid(True)

plt.tight_layout()
plt.show()
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X1, X2, Y, color='purple', s=60)

ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")
ax.set_title("3D Plot of X1, X2, Y")

plt.show()
