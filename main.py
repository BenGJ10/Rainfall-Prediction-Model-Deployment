import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load model and feature names
with open("Models/rainfall_prediction_model.pkl", "rb") as rf_model:
    model_data = pickle.load(rf_model)  # Load dictionary
    model = model_data["model"]  # Extract model
    feature_names = model_data["feature_names"]  # Extract feature names

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract data from form using feature names
        input_data = [float(request.form.get(col)) for col in feature_names]

        # Convert to DataFrame with correct column names
        input_df = pd.DataFrame([input_data], columns=feature_names)

        # Make prediction
        prediction = model.predict(input_df)[0]

        return render_template("result.html", prediction=round(prediction, 2))
    
    except ValueError:
        return render_template("result.html", error="Invalid input. Please enter valid numerical values.")
    except Exception as e:
        return render_template("result.html", error=f"An error occurred: {str(e)}")

@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        # Ensure the JSON contains all required features
        input_df = pd.DataFrame([data], columns=feature_names)

        # Make prediction
        prediction = model.predict(input_df)[0]
        
        return jsonify({"prediction": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5001, debug=True)
