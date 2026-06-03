# src/predict.py

import joblib
import pandas as pd

# LOAD TRAINED MODEL

MODEL_PATH = r"D:\FOR VS CODE\ML_projects\Energy-Optimization-Engine\energy_model.pkl"

model = joblib.load(MODEL_PATH)

print("Model Loaded Successfully")

# USER INPUTS
hour = int(input("Enter Hour (0-23): "))
day_type = int(input("Enter Day Type (0=Weekday, 1=Weekend): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
occupancy = int(input("Enter Occupancy (%): "))
current_energy = float(input("Enter Current Energy Consumption (kWh): "))

# CREATE INPUT DATAFRAME
input_data = pd.DataFrame({
    "hour": [hour],
    "day_type": [day_type],
    "temperature": [temperature],
    "humidity": [humidity],
    "occupancy": [occupancy],
    "current_energy": [current_energy]
})

# PREDICTION
prediction = model.predict(input_data)

print("\n===== PREDICTION RESULT =====")
print(f"Predicted Optimized Energy: {prediction[0]:.2f} kWh")