import os
import requests
import math

# Google Maps Geocoding API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_GEOCODING_API_KEY")

def geocode_address(address: str):
    """Geocodes a given address using the Google Maps Geocoding API."""
    if not GOOGLE_API_KEY:
        raise ValueError("Google Maps API key not set in environment variable.")

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200 or data.get("status") != "OK":
        raise ValueError(f"Failed to geocode '{address}': {data.get('error_message') or data.get('status')}")

    location = data["results"][0]["geometry"]["location"]
    return location["lat"], location["lng"]

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """Calculates distance between two lat/lon pairs using the Haversine formula."""
    R = 6371.0  # Earth radius in kilometers

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_phi / 2) ** 2 +
        math.cos(phi1) * math.cos(phi2) *
        math.sin(delta_lambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    kilometers = R * c
    miles = kilometers * 0.621371

    return round(kilometers, 2), round(miles, 2)
