# ============================================================
# 🌍 WEATHER FORECAST & ALERT DASHBOARD
# File: app.py
# ============================================================

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from dotenv import load_dotenv
from datetime import datetime
import os

# ============================================================
# LOAD API KEY
# ============================================================

load_dotenv()

API_KEY = os.getenv("API_KEY")

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Weather Intelligence Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

custom_css = """
<style>

/* Main Background */

[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
}

/* Hide Streamlit Header */

header {
    visibility: hidden;
}

/* Text Styling */

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

/* Weather Cards */

.weather-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 10px;
}

/* Button */

.stButton > button {
    background-color: #1F77FF;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

/* Selectbox */

div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ============================================================
# TITLE
# ============================================================

st.markdown("""
<h1 style='text-align:center; font-size:55px;'>
🌍 Weather Forecast & Alert Dashboard
</h1>

<h3 style='text-align:center;'>
Real-Time Climate Intelligence Platform
</h3>
""", unsafe_allow_html=True)

st.write("")

# ============================================================
# COUNTRY & CITY OPTIONS
# ============================================================

city_options = {

    "India": [
        "Bengaluru",
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Chennai",
        "Kolkata"
    ],

    "USA": [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston"
    ],

    "UK": [
        "London",
        "Manchester",
        "Liverpool"
    ],

    "Canada": [
        "Toronto",
        "Vancouver"
    ],

    "Australia": [
        "Sydney",
        "Melbourne"
    ]
}

# ============================================================
# SEARCH PANEL
# ============================================================

st.markdown("## 🔎 Search Weather")

col1, col2 = st.columns(2)

with col1:

    country = st.selectbox(
        "🌍 Select Country",
        list(city_options.keys())
    )

with col2:

    city = st.selectbox(
        "🏙️ Select City",
        city_options[country]
    )

# ============================================================
# SESSION STATE FIX
# ============================================================

if "weather_loaded" not in st.session_state:
    st.session_state.weather_loaded = False

if st.button("🚀 Get Weather Insights"):
    st.session_state.weather_loaded = True

# ============================================================
# FETCH WEATHER DATA
# ============================================================

def fetch_weather(city):

    current_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    forecast_url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    current_response = requests.get(current_url)

    forecast_response = requests.get(forecast_url)

    if (
        current_response.status_code == 200 and
        forecast_response.status_code == 200
    ):

        return (
            current_response.json(),
            forecast_response.json()
        )

    else:
        return None, None

# ============================================================
# MAIN WEATHER DASHBOARD
# ============================================================

if st.session_state.weather_loaded:

    with st.spinner("Fetching live weather data..."):

        current_data, forecast_data = fetch_weather(city)

    if current_data:

        # ====================================================
        # EXTRACT WEATHER DATA
        # ====================================================

        temperature = current_data["main"]["temp"]

        humidity = current_data["main"]["humidity"]

        pressure = current_data["main"]["pressure"]

        wind_speed = current_data["wind"]["speed"]

        weather = current_data["weather"][0]["main"]

        description = current_data["weather"][0]["description"]

        visibility = current_data.get("visibility", 0) / 1000

        latitude = current_data["coord"]["lat"]

        longitude = current_data["coord"]["lon"]

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # ====================================================
        # WEATHER ICONS
        # ====================================================

        weather_icons = {

            "Clear": "☀️",

            "Clouds": "☁️",

            "Rain": "🌧️",

            "Thunderstorm": "⛈️",

            "Snow": "❄️",

            "Mist": "🌫️"
        }

        icon = weather_icons.get(weather, "🌍")

        
         # ====================================================
        # HERO SECTION
            # ====================================================

        st.markdown(
        f"""
        <div style="
        background: rgba(255,255,255,0.08);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
        ">

        <div style="
            font-size: 90px;
            margin-bottom: -20px;
        ">
            {icon}
        </div>

        <div style="
            font-size: 70px;
            font-weight: bold;
            color: white;
        ">
            {temperature}°C
        </div>

        <div style="
            font-size: 32px;
            color: white;
            font-weight: 600;
        ">
            {city}, {country}
        </div>

        <div style="
            font-size: 24px;
            color: #CCCCCC;
            margin-top: 10px;
        ">
            {description.title()}
        </div>

        <div style="
            font-size: 14px;
            color: gray;
            margin-top: 15px;
        ">
            Last Updated: {current_time}
        </div>

        </div>
        """,
         unsafe_allow_html=True
        )   
        # ====================================================
        # WEATHER CARDS
        # ====================================================

        st.markdown("## 📊 Live Weather Metrics")

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.markdown(f"""
            <div class="weather-card">
                <h3>💧 Humidity</h3>
                <h1>{humidity}%</h1>
            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""
            <div class="weather-card">
                <h3>💨 Wind Speed</h3>
                <h1>{wind_speed} m/s</h1>
            </div>
            """, unsafe_allow_html=True)

        with c3:

            st.markdown(f"""
            <div class="weather-card">
                <h3>🧭 Pressure</h3>
                <h1>{pressure}</h1>
            </div>
            """, unsafe_allow_html=True)

        with c4:

            st.markdown(f"""
            <div class="weather-card">
                <h3>👀 Visibility</h3>
                <h1>{visibility} km</h1>
            </div>
            """, unsafe_allow_html=True)

        # ====================================================
        # ALERTS
        # ====================================================

        st.markdown("## ⚠️ Weather Alerts")

        alerts = []

        if temperature > 38:
            alerts.append("🔥 Heatwave Alert Detected")

        if humidity > 85:
            alerts.append("💧 High Humidity Detected")

        if weather.lower() in [
            "rain",
            "thunderstorm",
            "drizzle"
        ]:
            alerts.append("🌧️ Rainfall Expected")

        if wind_speed > 15:
            alerts.append("💨 Strong Winds Detected")

        if alerts:

            for alert in alerts:
                st.warning(alert)

        else:

            st.success("✅ No Severe Weather Alerts")

        # ====================================================
        # GLOBAL MAP
        # ====================================================

        st.markdown("## 🌍 Global Weather Map")

        weather_map = folium.Map(
            location=[latitude, longitude],
            zoom_start=8
        )

        folium.Marker(
            [latitude, longitude],

            popup=f"{city} Weather Location",

            tooltip=city,

            icon=folium.Icon(
                color="blue",
                icon="cloud"
            )

        ).add_to(weather_map)

        st_folium(
            weather_map,
            width=1400,
            height=500
        )

        # ====================================================
        # FORECAST ANALYSIS
        # ====================================================

        forecast_list = forecast_data["list"]

        forecast_times = []

        forecast_temps = []

        forecast_humidity = []

        rainfall = []

        for item in forecast_list[:12]:

            forecast_times.append(
                item["dt_txt"]
            )

            forecast_temps.append(
                item["main"]["temp"]
            )

            forecast_humidity.append(
                item["main"]["humidity"]
            )

            rain = item.get(
                "rain",
                {}
            ).get("3h", 0)

            rainfall.append(rain)

        forecast_df = pd.DataFrame({

            "Time": forecast_times,

            "Temperature": forecast_temps,

            "Humidity": forecast_humidity,

            "Rainfall": rainfall
        })

        # ====================================================
        # TEMPERATURE GRAPH
        # ====================================================

        st.markdown("## 📈 Temperature Forecast")

        temp_fig = px.line(
            forecast_df,
            x="Time",
            y="Temperature",
            markers=True,
            title="Temperature Forecast Trend"
        )

        st.plotly_chart(
            temp_fig,
            use_container_width=True
        )

        # ====================================================
        # HUMIDITY GRAPH
        # ====================================================

        st.markdown("## 💧 Humidity Forecast")

        humidity_fig = px.bar(
            forecast_df,
            x="Time",
            y="Humidity",
            title="Humidity Analysis"
        )

        st.plotly_chart(
            humidity_fig,
            use_container_width=True
        )

        # ====================================================
        # RAINFALL GRAPH
        # ====================================================

        st.markdown("## 🌧️ Rainfall Prediction")

        rain_fig = px.area(
            forecast_df,
            x="Time",
            y="Rainfall",
            title="Rainfall Forecast"
        )

        st.plotly_chart(
            rain_fig,
            use_container_width=True
        )

        # ====================================================
        # AI INSIGHTS
        # ====================================================

        st.markdown("## 🧠 AI Weather Insights")

        insights = []

        if temperature > 35:
            insights.append(
                "🌡️ High temperature may cause dehydration."
            )

        if humidity > 80:
            insights.append(
                "💧 Humidity levels are uncomfortable today."
            )

        if weather.lower() == "rain":
            insights.append(
                "🌧️ Outdoor activities not recommended."
            )

        if wind_speed > 10:
            insights.append(
                "💨 Strong winds may affect travel."
            )

        if pressure < 1000:
            insights.append(
                "🧭 Low atmospheric pressure detected."
            )

        if insights:

            for insight in insights:
                st.info(insight)

        else:

            st.success(
                "✅ Weather conditions appear stable."
            )

        # ====================================================
        # WEATHER DATA TABLE
        # ====================================================

        st.markdown("## 📋 Detailed Weather Dataset")

        detailed_df = pd.DataFrame({

            "City": [city],

            "Country": [country],

            "Temperature": [temperature],

            "Humidity": [humidity],

            "Pressure": [pressure],

            "Wind Speed": [wind_speed],

            "Weather": [weather],

            "Description": [description],

            "Visibility": [visibility]
        })

        st.dataframe(
            detailed_df,
            use_container_width=True
        )

        # ====================================================
        # DOWNLOAD REPORT
        # ====================================================

        st.markdown("## 📥 Download Weather Report")

        csv = detailed_df.to_csv(index=False)

        st.download_button(
            label="⬇️ Download CSV Report",
            data=csv,
            file_name=f"{city}_weather_report.csv",
            mime="text/csv"
        )

    else:

        st.error("❌ Failed to Fetch Weather Data")

        st.info(
            "Possible Reasons:\n"
            "- Invalid API Key\n"
            "- API Key Not Activated Yet\n"
            "- Internet Connection Issue"
        )