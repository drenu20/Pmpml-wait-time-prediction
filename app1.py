import streamlit as st
import pandas as pd
import joblib
from geopy.distance import geodesic

# --- Load Assets ---
@st.cache_resource
def load_assets():
    model = joblib.load('pmpml_segment_model.pkl')
    le = joblib.load('traffic_encoder.pkl')
    stops_df = pd.read_csv('stop_locations.csv')
    routes_df = pd.read_csv('route_master.csv')
    return model, le, stops_df, routes_df

model, le, stops_df, routes_df = load_assets()

# --- Page Config ---
st.set_page_config(page_title="Pune PMPML Live Predictor", layout="wide", page_icon="🚌")
st.title("🚌 Pune PMPML: Intelligent Wait-Time Predictor")

# --- Sidebar Geolocation ---
st.sidebar.header("📍 Find Nearest Stop")

if st.sidebar.button("Scan My Location"):
    user_lat, user_lon = 18.5204, 73.8567

    stops_df['dist'] = stops_df.apply(
        lambda x: geodesic((user_lat, user_lon), (x.lat, x.lon)).meters,
        axis=1
    )

    nearest = stops_df.loc[stops_df['dist'].idxmin()]

    st.sidebar.success(f"Nearest Stop: {nearest['stop_name']}")
    st.sidebar.write(f"Distance: {nearest['dist']:.1f} meters away")

# --- Main Interface ---
st.subheader("Plan Your Journey")

route_list = sorted(routes_df['route_no'].unique())
selected_route = st.selectbox("Select Your Bus Route", route_list)

seq_str = routes_df[routes_df['route_no'] == selected_route]['stop_sequence'].iloc[0]
stop_ids = [int(s) for s in seq_str.split(',')]

route_stop_names = []
for sid in stop_ids:
    name_row = stops_df[stops_df['stop_id'] == sid]
    name = name_row['stop_name'].iloc[0] if not name_row.empty else f"Stop {sid}"
    route_stop_names.append(name)

name_to_id = dict(zip(route_stop_names, stop_ids))

col1, col2 = st.columns(2)

with col1:
    bus_at = st.selectbox("Current Bus Location", route_stop_names)
    hour = st.slider("Current Hour", 0, 23, 12)

with col2:
    user_at = st.selectbox("Your Boarding Stop", route_stop_names)
    traffic = st.select_slider(
        "Traffic Condition",
        options=['Very smooth', 'Smooth', 'Mild congestion', 'Heavy congestion']
    )

# --- Prediction ---
if st.button("Predict Arrival Time"):
    bus_idx = route_stop_names.index(bus_at)
    user_idx = route_stop_names.index(user_at)

    if bus_idx >= user_idx:
        st.error("⚠️ The bus has already passed your stop!")
    else:
        with st.spinner('Calculating live traffic segments...'):
            total_wait = 0
            t_enc = le.transform([traffic])[0]

            for i in range(bus_idx, user_idx):
                s_from, s_to = stop_ids[i], stop_ids[i+1]
                pred = model.predict([[s_from, s_to, hour, t_enc, 1.5]])[0]
                total_wait += pred

            st.success(f"### 🕒 Estimated Wait Time: {total_wait:.2f} Minutes")
            st.info(f"Bus is {user_idx - bus_idx} stops away from you.")
            st.balloons()
