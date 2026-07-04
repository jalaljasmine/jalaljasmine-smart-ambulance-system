import warnings
warnings.filterwarnings("ignore")


from models.predict_severity import predict
from models.hospital_score import recommend_hospital
from routing.check_traffic import predict_traffic
from routing.dijkstra import calculate_route

print("====== SMART AMBULANCE SYSTEM ======")

# 1. Accident Severity
severity = predict(None)
print("\nPredicted Severity:", severity)

# 2. Best Hospital
hospital = recommend_hospital(severity)

# 3. Traffic Prediction
input_data = [[9, 2, 7, 1, 3]]
traffic = predict_traffic(input_data)

print("\nPredicted Traffic:", traffic)

# 4. Route
route, distance, time = calculate_route(traffic)

print("\n========== FINAL RESULT ==========")
print("Severity :", severity)
print("Hospital :", hospital["Hospital"])
print("Distance :", round(distance/1000,2), "km")
print("Time :", round(time,2), "minutes")
print("==================================")