
# Import required libraries
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize the Flask application
superkart_api = Flask("SuperKart")

# Load the trained SuperKart model
model = joblib.load("superkart_model.joblib")


# Home route to check whether the API is running
@superkart_api.get("/")
def home():
    return "Welcome to the SuperKart Sales Prediction System"


# API endpoint to predict sales for a single product
@superkart_api.post("/v1/predict")
def predict_sales():

    # Get input data sent in JSON format
    data = request.get_json()

    # Prepare the input features required by the trained model
    sample = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_MRP": data["Product_MRP"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"],
        "Product_Id_char": data["Product_Id_char"],
        "Store_Age_Years": data["Store_Age_Years"],
        "Product_Type_Category": data["Product_Type_Category"]
    }

    # Convert the input into a DataFrame
    sample_df = pd.DataFrame([sample])

    # Generate the sales prediction
    prediction = model.predict(sample_df)[0]

    # Return the prediction as JSON
    return jsonify({
        "predicted_product_store_sales": round(float(prediction), 2)
    })


# Run the Flask application
if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=5000)
