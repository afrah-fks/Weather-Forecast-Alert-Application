import requests
from src.config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):

    print("\n========== DEBUG INFO ==========")

    print("Loaded API Key:", API_KEY)

    url = (
        f"{BASE_URL}"
        f"?q={city}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    print("\nGenerated URL:")
    print(url)

    try:

        response = requests.get(url)

        print("\nStatus Code:")
        print(response.status_code)

        print("\nAPI Response:")
        print(response.text)

        if response.status_code == 200:
            return response.json()

        else:
            return None

    except Exception as e:

        print("\nERROR:")
        print(e)

        return None
    