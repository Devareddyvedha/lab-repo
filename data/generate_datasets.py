"""
Generates the datasets used throughout the lab experiments.
Run once: python data/generate_datasets.py
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

np.random.seed(42)
N = 200

def make_diabetes_like(n, seed):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "Pregnancies": rng.integers(0, 15, n),
        "Glucose": rng.normal(120, 30, n).clip(50, 200).round(0),
        "BloodPressure": rng.normal(70, 15, n).clip(40, 120).round(0),
        "SkinThickness": rng.normal(25, 10, n).clip(5, 60).round(0),
        "Insulin": rng.normal(120, 90, n).clip(0, 400).round(0),
        "BMI": rng.normal(32, 7, n).clip(15, 55).round(2),
        "DiabetesPedigreeFunction": rng.gamma(2, 0.3, n).round(3),
        "Age": rng.integers(21, 81, n),
    })
    # Outcome loosely correlated with glucose/BMI so models have something to find
    score = (df["Glucose"] - 120) / 30 + (df["BMI"] - 32) / 7 + rng.normal(0, 1, n)
    df["Outcome"] = (score > 0).astype(int)
    return df

# UCI-style and Pima-style diabetes datasets
uci_diabetes = make_diabetes_like(N, seed=1)
pima_diabetes = make_diabetes_like(N, seed=2)
uci_diabetes.to_csv("data/uci_diabetes.csv", index=False)
pima_diabetes.to_csv("data/pima_diabetes.csv", index=False)

# Time series version (glucose over time, with trend + seasonality)
t = np.arange(N)
seasonal = 10 * np.sin(2 * np.pi * t / 30)
trend = 0.05 * t
ts_glucose = 120 + trend + seasonal + np.random.normal(0, 5, N)
diabetes9 = uci_diabetes.copy()
diabetes9["Glucose"] = ts_glucose.round(1)
diabetes9.to_csv("data/diabetes9.csv", index=False)

# Iris dataset
iris = load_iris(as_frame=True)
iris_df = iris.frame.rename(columns={
    "sepal length (cm)": "sepal length (cm)",
    "sepal width (cm)": "sepal width (cm)",
    "petal length (cm)": "petal length (cm)",
    "petal width (cm)": "petal width (cm)",
})
iris_df["species"] = iris_df["target"].map(dict(enumerate(iris.target_names)))
iris_df = iris_df.drop(columns=["target"])
iris_df.to_csv("data/iris_dataset.csv", index=False)

# Small generic CSV/Excel for the "reading data" experiment
generic = pd.DataFrame({
    "Product": ["Laptop", "Smartphone", "Tablet", "Headphones"],
    "Price": [1000, 800, 500, 100],
    "Quantity": [5, 8, 10, 15],
})
generic["existing_column"] = generic["Price"]
generic["another_column"] = generic["Quantity"]
generic["category_column"] = generic["Product"]
generic["numeric_column"] = generic["Price"]
generic["column1"] = generic["Product"]
generic["column2"] = generic["Price"]
generic.to_csv("data/data.csv", index=False)
generic.to_excel("data/data.xlsx", index=False, sheet_name="Sheet1")

print("Datasets written to data/")
