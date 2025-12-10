import numpy as np
from sklearn.linear_model import LinearRegression


X1 = [60, 62, 67, 70, 71, 72, 75,78]
X2 = [22,25,24,20,15,14,14,11]
Y  = [140,155,159,179,192,200,212,215]


X = np.column_stack((X1, X2))


model = LinearRegression()


model.fit(X, Y)


print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)


new = [[80, 24]]    
print("Prediction for X1=80, X2=24 →", model.predict(new))
