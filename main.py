from src.api_handler import fetch_weather
from src.parser import parse_weather_data
from src.alerts import generate_alerts
from src.visualization import create_weather_chart
from src.report_generator import save_weather_report
from src.utils import print_separator


def main():

    city = input("Enter city name: ")

    # Fetch API data
    raw_data = fetch_weather(city)

    if raw_data:

        # Parse data
        weather_data = parse_weather_data(raw_data)

        # Generate alerts
        alerts = generate_alerts(weather_data)

        # Create chart
        chart_path = create_weather_chart(weather_data)

        # Save report
        report_path = save_weather_report(weather_data, alerts)

        # Display output
        print_separator()

        print("WEATHER REPORT")

        print_separator()

        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather: {weather_data['weather']}")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

        print_separator()

        print("ALERTS")

        print_separator()

        if alerts:
            for alert in alerts:
                print(alert)
        else:
            print("No severe alerts")

        print_separator()

        print(f"Chart saved: {chart_path}")
        print(f"Report saved: {report_path}")

    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    main()