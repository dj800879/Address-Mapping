import requests
from math import radians, cos, sin, sqrt, atan2
import logging
import time

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Geocode address using OpenStreetMap's Nominatim API with retry + logging
def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "delivery-distance-app"
    }

    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()

            if not data:
                raise ValueError(f"No geocoding result for address: {address}")

            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return lat, lon

        except Exception as e:
            logger.warning(f"Attempt {attempt + 1} - Failed to geocode '{address}': {e}")
            if attempt < retries - 1:
                time.sleep(1)  # backoff before retry
            else:
                raise

# Calculate distance between two coordinates using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R_km = 6371  # Earth radius in kilometers

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)

    a = sin(d_lat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance_km = R_km * c
    distance_mi = distance_km * 0.621371

    return round(distance_km, 2), round(distance_mi, 2)
