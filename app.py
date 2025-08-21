import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------
# Load trained pipeline
# ---------------------------
@st.cache_resource
def load_model():
    model_dict = joblib.load("best_carprice_model.joblib")  # ensure file is in same dir
    return model_dict["pipeline"]

pipe = load_model()

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

st.title("🚗 Car Price Prediction App")
st.write("Fill all car details from sidebar to get estimated car price prediction.")

# ---------------------------
# Sidebar Inputs (All 33 Columns)
# ---------------------------
st.sidebar.header("Car Features Input")
# categorical sets
carcompanies = [
    'chevrolet','isuzu','subaru','volkswagen','alfa-romero','honda','toyota','renault',
    'mazda','buick','porsche','bmw','jaguar','mitsubishi','saab','audi','volvo',
    'dodge','nissan','mercury','plymouth','peugeot'
]

carmodels = [
    'dodge_wagon','audi_wagon','bmw_sedan','volkswagen_hatchback','toyota_wagon',
    'peugeot_wagon','chevrolet_sedan','mazda_hatchback','honda_hatchback','porsche_convertible',
    'jaguar_sedan','buick_convertible','saab_hatchback','alfa-romero_convertible','toyota_hatchback',
    'nissan_wagon','porsche_hardtop','renault_hatchback','volkswagen_wagon','audi_hatchback',
    'plymouth_sedan','chevrolet_hatchback','honda_sedan','mazda_sedan','nissan_sedan',
    'porsche_hatchback','volkswagen_sedan','renault_wagon','isuzu_hatchback','buick_wagon',
    'plymouth_wagon','volvo_wagon','subaru_sedan','plymouth_hatchback','honda_wagon',
    'alfa-romero_hatchback','nissan_hardtop','volvo_sedan','subaru_hatchback','buick_hardtop',
    'dodge_hatchback','peugeot_sedan','mitsubishi_sedan','nissan_hatchback','mercury_hatchback',
    'subaru_wagon','audi_sedan','volkswagen_convertible','dodge_sedan','toyota_sedan',
    'saab_sedan','mitsubishi_hatchback','toyota_convertible','toyota_hardtop','buick_sedan','isuzu_sedan'
]
row = {}

row["carcompany"] = st.sidebar.selectbox("Car Company", carcompanies)
row["carmodels"] = st.sidebar.selectbox("Car Model", carmodels)
row["fueltype"] = st.sidebar.selectbox("Fuel Type", ["gas", "diesel"])
row["aspiration"] = st.sidebar.selectbox("Aspiration", ["std", "turbo"])
row["enginesize"] = st.sidebar.number_input("Engine Size (cc)", 60, 400, 130)
row["curbweight"] = st.sidebar.number_input("Curb Weight", 1500, 5000, 2500)
row["horsepower"] = st.sidebar.number_input("Horsepower", 40, 300, 100)
row["carwidth"] = st.sidebar.number_input("Car Width", 60.0, 75.0, 65.0)
row["carlength"] = st.sidebar.number_input("Car Length", 140.0, 210.0, 170.0)
row["wheelbase"] = st.sidebar.number_input("Wheelbase", 80.0, 120.0, 100.0)
row["stroke"] = st.sidebar.number_input("Stroke", 2.0, 5.0, 3.2)
row["compressionratio"] = st.sidebar.number_input("Compression Ratio", 7.0, 23.0, 9.0)
row["carbody"] = st.sidebar.selectbox("Car Body", ["sedan", "hatchback", "wagon", "hardtop", "convertible"])
row["drivewheel"] = st.sidebar.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
row["enginelocation"] = st.sidebar.selectbox("Engine Location", ["front", "rear"])
row["enginetype"] = st.sidebar.selectbox("Engine Type", ["ohc","ohcf","ohcv","l","dohc","rotor"])
row["cylindernumber"] = st.sidebar.selectbox("Cylinders", ["two","three","four","five","six","eight","twelve"])
row["fuelsystem"] = st.sidebar.selectbox("Fuel System", ["mpfi","2bbl","1bbl","4bbl","idi","spdi","spfi"])
row["is_luxury"] = st.sidebar.selectbox("Is Luxury (Category)", ["luxury","standard"])


row["peakrpm"] = st.sidebar.number_input("Peak RPM", 4000, 7000, 5000)
row["citympg"] = st.sidebar.number_input("City MPG", 10, 60, 25)
row["highwaympg"] = st.sidebar.number_input("Highway MPG", 10, 60, 30)
row["fueltype_num"] = st.sidebar.selectbox("Fuel Type Num (0=Gas,1=Diesel)", [0,1])
row["is_luxury_flag"] = st.sidebar.selectbox("Luxury Flag (1=Yes,0=No)", [0,1])


row["carheight"] = st.sidebar.number_input("Car Height", 47.0, 60.0, 54.0)
row["boreratio"] = st.sidebar.number_input("Bore Ratio", 2.0, 4.0, 3.0)
row["power_to_weight"] = st.sidebar.number_input("Power-to-Weight", 0.0, 1.0, 0.04)
row["avg_mpg"] = st.sidebar.number_input("Average MPG", 10.0, 60.0, 27.5)
row["bore_stroke_ratio"] = st.sidebar.number_input("Bore/Stroke Ratio", 0.0, 2.0, 1.0)
row["length_width"] = st.sidebar.number_input("Length * Width", 8000.0, 15000.0, 11050.0)
row["hp_per_cc"] = st.sidebar.number_input("HP per CC", 0.0, 2.0, 0.7)
row["hp_x_width"] = st.sidebar.number_input("HP × Width", 2000.0, 20000.0, 6500.0)
row["engine_per_weight"] = st.sidebar.number_input("Engine per Weight", 0.0, 0.2, 0.05)

# ---------------------------
# Convert to DataFrame
# ---------------------------
X_in = pd.DataFrame([row])

# ---------------------------
# Prediction
# ---------------------------
if st.button("🔮 Predict Price"):
    log_price_pred = pipe.predict(X_in)[0]
    price_pred = np.expm1(log_price_pred)
    st.success(f"💰 Estimated Price: ${price_pred:,.0f}")
    st.caption("Prediction is based on log(price) → back-transformed for actual price.")
