# src/train_model.py

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# LOAD DATASET

DATA_PATH = r"D:\FOR VS CODE\ML_projects\Energy-Optimization-Engine\dataset\final_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully")
print(df.head())


# DATA PREPROCESSING
# Convert day_type to numeric
df["day_type"] = df["day_type"].map({
    "Weekday": 0,
    "Weekend": 1
})

# Features
X = df[
    [
        "hour",
        "day_type",
        "temperature",
        "humidity",
        "occupancy",
        "current_energy"
    ]
]

# Target
y = df["target_energy"]

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL TRAINING
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# EVALUATION
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print(f"MAE : {mae:.2f}")
print(f"R2 Score : {r2:.4f}")

# SAVE MODEL
MODEL_PATH = r"D:\FOR VS CODE\ML_projects\Energy-Optimization-Engine\energy_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel Saved Successfully")
print(MODEL_PATH)