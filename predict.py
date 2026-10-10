
import joblib
import pandas as pd

model = joblib.load("telecom_tower_model.pkl")

new_data = pd.DataFrame({
    "voltage": [11.2],
    "temperature_c": [55],
    "signal_drop_rate": [0.5],
    "cpu_usage": [88],
    "battery_health": [65],
    "network_latency_ms": [95]
})

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Hardware Failure Predicted")
else:
    print("Tower is Healthy")
