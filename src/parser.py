from datetime import datetime


def parse_weather_data(data):
    """
    Extract important weather information
    """

    parsed_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return parsed_data