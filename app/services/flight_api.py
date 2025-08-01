import os
import requests

FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")
FLIGHT_API_URL = "https://api.flightapi.io/schedule" + "/" + FLIGHT_API_KEY

async def get_flight_data(airport_code: str):
    params = {
        "mode": "arrivals",
        "iata": airport_code,
        "day": 1,
    }

    try:
        response = requests.get(FLIGHT_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching flight data: {e}")
        return None    