import matplotlib.pyplot as plt
import os


def create_weather_chart(weather_data):
    """
    Create weather visualization chart
    """

    labels = ["Temperature", "Humidity", "Wind Speed"]

    values = [
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["wind_speed"]
    ]

    plt.figure(figsize=(6, 4))

    plt.bar(labels, values)

    plt.title("Weather Analysis")

    plt.ylabel("Values")

    # Create output folder
    os.makedirs("outputs/charts", exist_ok=True)

    chart_path = "outputs/charts/weather_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path