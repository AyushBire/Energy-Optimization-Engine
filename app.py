import streamlit as st
import pandas as pd
import joblib

MODEL_PATH = r"D:\FOR VS CODE\ML_projects\Energy-Optimization-Engine\energy_model.pkl"

model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Energy Optimization Engine",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ AI Energy Optimization Engine")

hour = st.sidebar.slider("Hour", 0, 23, 10)

day_type = st.sidebar.selectbox(
    "Day Type",
    ["Weekday", "Weekend"]
)

temperature = st.sidebar.slider(
    "Temperature (°C)",
    15,
    45,
    30
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    20,
    100,
    60
)

occupancy = st.sidebar.slider(
    "Occupancy (%)",
    0,
    100,
    50
)

current_energy = st.sidebar.number_input(
    "Current Energy Consumption (kWh)",
    min_value=0.0,
    value=400.0
)

day_value = 0 if day_type == "Weekday" else 1

input_data = pd.DataFrame({
    "hour": [hour],
    "day_type": [day_value],
    "temperature": [temperature],
    "humidity": [humidity],
    "occupancy": [occupancy],
    "current_energy": [current_energy]
})

optimized_energy = model.predict(input_data)[0]

energy_saved = current_energy - optimized_energy

savings_percent = (energy_saved / current_energy) * 100

cost_saved = energy_saved * 10

if occupancy < 10:
    hvac_action = "Reduce HVAC by 40%"
elif occupancy < 20:
    hvac_action = "Reduce HVAC by 30%"
elif occupancy < 40:
    hvac_action = "Reduce HVAC by 20%"
else:
    hvac_action = "Maintain Current HVAC Settings"

col1, col2, col3 = st.columns(3)

col1.metric(
    "Current Energy",
    f"{current_energy:.2f} kWh"
)

col2.metric(
    "Optimized Energy",
    f"{optimized_energy:.2f} kWh"
)

col3.metric(
    "Energy Saved",
    f"{energy_saved:.2f} kWh"
)

st.divider()

st.metric(
    "Estimated Cost Saving",
    f"₹ {cost_saved:.2f}"
)

st.metric(
    "Savings Percentage",
    f"{savings_percent:.2f}%"
)

st.success(hvac_action)

chart_data = pd.DataFrame({
    "Energy": [
        current_energy,
        optimized_energy
    ]
},
index=[
    "Current",
    "Optimized"
])

st.bar_chart(chart_data)

st.subheader("System Summary")

st.write(f"""
Hour : {hour}

Day Type : {day_type}

Temperature : {temperature} °C

Humidity : {humidity} %

Occupancy : {occupancy} %

HVAC Recommendation : {hvac_action}
""")