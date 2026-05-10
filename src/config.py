from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# API Key
API_KEY = os.getenv("API_KEY")

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Alert Thresholds
TEMP_THRESHOLD = 38
HUMIDITY_THRESHOLD = 85
WIND_THRESHOLD = 15