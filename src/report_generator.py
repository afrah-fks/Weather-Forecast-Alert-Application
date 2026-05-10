import pandas as pd
import os


def save_weather_report(weather_data, alerts):
    """
    Save weather report as CSV
    """

    report = {
        "City": [weather_data["city"]],
        "Date_Time": [weather_data["date_time"]],
        "Temperature": [weather_data["temperature"]],
        "Humidity": [weather_data["humidity"]],
        "Pressure": [weather_data["pressure"]],
        "Weather": [weather_data["weather"]],
        "Description": [weather_data["description"]],
        "Wind Speed": [weather_data["wind_speed"]],
        "Alerts": [", ".join(alerts) if alerts else "No Alerts"]
    }

    df = pd.DataFrame(report)

    os.makedirs("outputs/reports", exist_ok=True)

    report_path = f"outputs/reports/{weather_data['city']}_report.csv"

    df.to_csv(report_path, index=False)

    return report_path