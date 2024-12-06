import requests

def get_geolocation(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()
        location = data.get("loc", "").split(",")
        latitude = location[0] if len(location) > 0 else None
        longitude = location[1] if len(location) > 1 else None
        city = data.get("city", "Неизвестно")

        return {
            "latitude": latitude,
            "longitude": longitude,
            "city": city
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None