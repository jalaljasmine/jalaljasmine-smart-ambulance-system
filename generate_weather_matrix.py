import pandas as pd
import numpy as np
import os

print("[GENERATOR] Initializing synthetic climate timeline linker...")

# Ensure datasets directory exists
os.makedirs("datasets", exist_ok=True)

# Load your actual traffic file timeline array references to match indices perfectly
try:
    traffic_df = pd.read_csv("datasets/traffic.csv")
    unique_timestamps = traffic_df['DateTime'].unique()
    print(f"[INFO] Extracting {len(unique_timestamps)} unique hourly map slots across your 2015-2017 timeline...")
except Exception as e:
    print("[WARNING] Could not read traffic.csv. Generating baseline dates as backup.")
    # Fallback to create dates from November 1st 2015 to June 30th 2017 hourly
    date_range = pd.date_range(start="2015-11-01 00:00:00", end="2017-06-30 23:00:00", freq="h")
    unique_timestamps = date_range.strftime('%Y-%m-%d %H:%M:%S')

# Generate realistic climate distributions matching your framework constraints
np.random.seed(42) # Keeps generation perfectly consistent
weather_choices = ["Clear", "Rainy", "Foggy"]
probabilities = [0.80, 0.15, 0.05] # 80% Clear, 15% Rain, 5% Fog

generated_states = np.random.choice(weather_choices, size=len(unique_timestamps), p=probabilities)

# Assign matching structural parameters based on state mapping conditions
visibility_metrics = []
precipitation_metrics = []
temperature_metrics = []

for state in generated_states:
    if state == "Rainy":
        visibility_metrics.append(round(np.random.uniform(2.5, 5.0), 1))
        precipitation_metrics.append(round(np.random.uniform(1.5, 12.0), 1))
        temperature_metrics.append(round(np.random.uniform(21.0, 24.5), 1))
    elif state == "Foggy":
        visibility_metrics.append(round(np.random.uniform(0.5, 1.9), 1))
        precipitation_metrics.append(0.0)
        temperature_metrics.append(round(np.random.uniform(18.0, 22.0), 1))
    else: # Clear
        visibility_metrics.append(10.0)
        precipitation_metrics.append(0.0)
        temperature_metrics.append(round(np.random.uniform(25.0, 34.0), 1))

# Pack data down into the target dataset template structures
weather_clean_df = pd.DataFrame({
    'DateTime': unique_timestamps,
    'Weather_State': generated_states,
    'Visibility_km': visibility_metrics,
    'Precipitation_mm': precipitation_metrics,
    'Temperature_C': temperature_metrics
})

# Export directly to your datasets folder workspace
weather_clean_df.to_csv("datasets/weather_clean.csv", index=False)
print("="*60)
print("[SUCCESS] Weather reference asset successfully created locally!")
print("Saved location : datasets/weather_clean.csv")
print(f"Total Entries  : {len(weather_clean_df)} continuous hourly rows")
print("="*60)
