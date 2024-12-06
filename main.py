import requests

def get_geolocation(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()
        return data
    except Exception as e:
        print(f"Ошибка: {e}")
        return None