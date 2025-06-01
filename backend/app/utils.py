import os
import requests
import math
from dotenv import load_dotenv

# Load environment variables from .env file (useful for local dev)
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_GEOCODING_API_KEY")


def geocode_address(address: str) -> tuple[float, float]:
    """
    Geocode an address using the Google Maps Geocoding API.
    Returns (latitude, longitude) tuple.
    """
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": GOOGLE_API_KEY
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["status"] != "OK":
            raise ValueError(f"Geocoding failed: {data.get('error_message', data['status'])}")

        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]

    except Exception as e:
        raise ValueError(f"Error during geocoding '{address}': {str(e)}")


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> tuple[float, float]:
    """
    Calculate distance between two lat/lon points using the Haversine formula.
    Returns distance in kilometers and miles.
    """
    R = 6371  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km = R * c
    distance_miles = distance_km * 0.621371

    return round(distance_km, 2), round(distance_miles, 2)