from src.config import (
    TEMP_THRESHOLD,
    HUMIDITY_THRESHOLD,
    WIND_THRESHOLD
)


def generate_alerts(weather_data):
    """
    Generate weather alerts
    """

    alerts = []

    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    weather = weather_data["weather"]

    # Heat alert
    if temperature > TEMP_THRESHOLD:
        alerts.append("🔥 Heatwave Alert")

    # Rain alert
    if weather.lower() in ["rain", "thunderstorm", "drizzle"]:
        alerts.append("🌧️ Rain Alert")

    # Humidity alert
    if humidity > HUMIDITY_THRESHOLD:
        alerts.append("💧 High Humidity Alert")

    # Wind alert
    if wind_speed > WIND_THRESHOLD:
        alerts.append("💨 Strong Wind Alert")

    return alerts