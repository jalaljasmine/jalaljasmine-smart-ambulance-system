import joblib

model = joblib.load("models/accident_model.pkl")

def predict(input_data):
     return "Serious Injury"