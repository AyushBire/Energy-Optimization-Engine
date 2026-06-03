# ⚡ Energy Optimization Engine

## Overview

The Energy Optimization Engine is a Machine Learning-based system designed to optimize energy consumption in commercial buildings. The project predicts optimized energy usage based on factors such as occupancy, temperature, humidity, and current energy consumption.

The system provides intelligent HVAC recommendations and estimates potential energy and cost savings, helping organizations reduce operational expenses and improve energy efficiency.

---

## Features

* Energy Consumption Prediction using Machine Learning
* HVAC Optimization Recommendations
* Cost Savings Estimation
* Occupancy-Based Energy Management
* Interactive Streamlit Dashboard
* Real-Time Building Parameter Simulation
* Energy Usage Visualization

---

## Problem Statement

Commercial buildings consume a significant amount of electricity through HVAC systems, lighting, and equipment. Most buildings operate on fixed schedules regardless of occupancy levels, resulting in energy waste and increased costs.

This project uses Machine Learning to analyze building conditions and recommend optimized energy usage strategies.

---

## Project Architecture

Input Parameters

* Occupancy Percentage
* Temperature
* Humidity
* Time of Day
* Day Type (Weekday/Weekend)
* Current Energy Consumption

↓

Machine Learning Model

(Random Forest Regressor)

↓

Energy Optimization Engine

↓

HVAC Recommendations

↓

Energy & Cost Savings Report

---

## Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Random Forest Regressor

### Data Processing

* Pandas
* NumPy

### Model Persistence

* Joblib

### Dashboard

* Streamlit

### Visualization

* Matplotlib

---

## Project Structure

```text
Energy-Optimization-Engine/
│
├── dataset/
│   └── final_dataset.csv
│
├── venv/
│
├── app.py
├── energy_model.pkl
├── train_model.py
├── predict.py
├── optimize.py
├── weather_api.py
└── README.md
```

---

## Dataset Features

| Feature        | Description                   |
| -------------- | ----------------------------- |
| hour           | Hour of the day               |
| day_type       | Weekday or Weekend            |
| temperature    | Ambient temperature           |
| humidity       | Relative humidity             |
| occupancy      | Building occupancy percentage |
| current_energy | Current energy consumption    |
| target_energy  | Optimized energy consumption  |

---

## Machine Learning Workflow

### Data Collection

Synthetic building energy dataset created for prototype development.

### Data Preprocessing

* Data cleaning
* Feature selection
* Encoding categorical variables

### Model Training

Random Forest Regressor is trained to predict optimized energy consumption.

### Optimization

The system calculates:

* Predicted Optimized Energy Usage
* Energy Savings
* Savings Percentage
* Estimated Cost Savings
* HVAC Adjustment Recommendations

---

## HVAC Optimization Logic

```python
if occupancy < 10:
    reduce_hvac = 40%

elif occupancy < 20:
    reduce_hvac = 30%

elif occupancy < 40:
    reduce_hvac = 20%

else:
    maintain_current_settings()
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Energy-Optimization-Engine.git
```

Navigate to the project directory:

```bash
cd Energy-Optimization-Engine
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn joblib streamlit matplotlib requests
```

---

## Run the Project

### Train Model

```bash
python train_model.py
```

### Prediction

```bash
python predict.py
```

### Optimization Report

```bash
python optimize.py
```

### Launch Dashboard

```bash
python -m streamlit run app.py
```

---

## Sample Output

* Current Energy Consumption
* Optimized Energy Consumption
* Energy Savings
* Cost Savings
* HVAC Recommendations

Example:

```text
Current Energy Usage: 450 kWh

Optimized Energy Usage: 390 kWh

Energy Saved: 60 kWh

Savings Percentage: 13.33%

Estimated Cost Savings: ₹600

HVAC Recommendation: Reduce HVAC by 20%
```

---

## Future Enhancements

* Live Weather API Integration
* Real-Time IoT Sensor Support
* Smart Building Management System Integration
* Reinforcement Learning-Based Optimization
* Carbon Footprint Analysis
* Predictive Maintenance for HVAC Systems

---

## Resume Description

Developed an AI-based Energy Optimization Engine using Machine Learning to predict building energy consumption and recommend HVAC optimization strategies. Implemented a Random Forest regression model, occupancy-based optimization logic, and an interactive Streamlit dashboard to estimate energy savings and reduce operational costs.

---

## Author

Ayush Bire

B.Tech CSE (Artificial Intelligence & Machine Learning)

G.H. Raisoni College of Engineering, Nagpur
