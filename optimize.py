# src/optimize.py

import joblib
import pandas as pd

# LOAD MODEL
MODEL_PATH = r"D:\FOR VS CODE\ML_projects\Energy-Optimization-Engine\energy_model.pkl"

model = joblib.load(MODEL_PATH)

# USER INPUTS
hour = int(input("Enter Hour (0-23): "))
day_type = int(input("Enter Day Type (0=Weekday, 1=Weekend): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
occupancy = int(input("Enter Occupancy (%): "))
current_energy = float(input("Enter Current Energy Consumption (kWh): "))

# CREATE INPUT DATA
input_data = pd.DataFrame({
    "hour": [hour],
    "day_type": [day_type],
    "temperature": [temperature],
    "humidity": [humidity],
    "occupancy": [occupancy],
    "current_energy": [current_energy]
})

# PREDICTION
optimized_energy = model.predict(input_data)[0]

# SAVINGS CALCULATION
energy_saved = current_energy - optimized_energy

savings_percent = (
    energy_saved / current_energy
) * 100

# Electricity Cost
# Assuming ₹10 per kWh

cost_per_kwh = 10

cost_saved = energy_saved * cost_per_kwh

# HVAC RECOMMENDATION
if occupancy < 10:
    hvac_action = "Reduce HVAC by 40%"
elif occupancy < 20:
    hvac_action = "Reduce HVAC by 30%"
elif occupancy < 40:
    hvac_action = "Reduce HVAC by 20%"
else:
    hvac_action = "Maintain Current HVAC Settings"

# RESULTS
print("\n========== ENERGY OPTIMIZATION REPORT ==========")

print(f"\nCurrent Energy Usage : {current_energy:.2f} kWh")

print(f"Optimized Energy Usage : {optimized_energy:.2f} kWh")

print(f"Energy Saved : {energy_saved:.2f} kWh")

print(f"Savings Percentage : {savings_percent:.2f}%")

print(f"Estimated Cost Savings : ₹{cost_saved:.2f}")

print(f"HVAC Recommendation : {hvac_action}")

print("\n===============================================")