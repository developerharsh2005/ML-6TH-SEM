import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

dataset_path = r"C:\Users\KIIT0001\Desktop\ipl.csv"
target_column = "winner"

df = pd.read_csv(dataset_path)

df = df.dropna(subset=[target_column])

X = df.drop(columns=[target_column])
y = df[target_column]

X = pd.get_dummies(X, drop_first=True)

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression": LogisticRegression(max_iter=5000),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(kernel="rbf")
}

results = []

print("\n========= CLASSIFICATION MODELS COMPARISON =========\n")

for name, model in models.items():
    if name in ["KNN", "Logistic Regression", "SVM"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    results.append([name, acc])

    print(f"Model: {name}")
    print("Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("-" * 50)

df_results = pd.DataFrame(results, columns=["Algorithm", "Accuracy"])
df_results = df_results.sort_values(by="Accuracy", ascending=False)

print("\n========= FINAL ACCURACY COMPARISON TABLE =========\n")
print(df_results)
