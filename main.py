import requests

def get_geolocation(ip_address):
    try:
        # Отправка запроса к API ipinfo.io
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()

        # Извлечение данных о местоположении
        location = data.get("loc", "").split(",")
        latitude = location[0] if len(location) > 0 else None
        longitude = location[1] if len(location) > 1 else None
        city = data.get("city", "Неизвестно")

        # Возврат результатов
        return {
            "latitude": latitude,
            "longitude": longitude,
            "city": city
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Пример использования функции
if __name__ == "__main__":
    ip = "8.8.8.8"  # Пример IP-адреса
    geolocation = get_geolocation(ip)

    if geolocation:
        print(f"Широта: {geolocation['latitude']}")
        print(f"Долгота: {geolocation['longitude']}")
        print(f"Город: {geolocation['city']}")
    else:
        print("Не удалось получить информацию о местоположении.")