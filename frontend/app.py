
import streamlit as st
import requests

# Backend API URL
BACKEND_URL = "http://backend:7860"

# Page title
st.title("SuperKart Sales Prediction System")

st.write(
    "Enter the product and store details below to predict the total sales."
)

# Input fields for product and store information
Product_Weight = st.number_input(
    "Product Weight", min_value=0.0, value=12.66
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area", min_value=0.0, value=0.027
)

Product_MRP = st.number_input(
    "Product MRP", min_value=0.0, value=117.08
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    ["Supermarket Type1", "Supermarket Type2",
     "Supermarket Type3", "Departmental Store"]
)

Product_Id_char = st.selectbox(
    "Product ID Character",
    ["FD", "DR", "NC"]
)

Store_Age_Years = st.number_input(
    "Store Age (Years)", min_value=0, value=16
)

Product_Type_Category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

# Prepare JSON data for the backend API
product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

# Send data to the backend when the button is clicked
if st.button("Predict Sales"):
    try:
        response = requests.post(
            f"{BACKEND_URL}/v1/predict",
            json=product_data
        )

        if response.status_code == 200:
            prediction = response.json()
            st.success(
                f"Predicted Sales: "
                f"{prediction['predicted_product_store_sales']}"
            )
        else:
            st.error("Unable to generate prediction.")

    except requests.exceptions.RequestException:
        st.error("Unable to connect to the backend API.")
