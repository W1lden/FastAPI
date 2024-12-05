import requests
from app.config import OPENWEATHER_API_KEY


class OpenWeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city: str) -> dict:
        """
        Получает данные о погоде для указанного города через OpenWeather API.
        """
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
        }

        try:
            response = requests.get(OpenWeatherService.BASE_URL, params=params)
            response.raise_for_status()  # Проверяем, был ли успешным HTTP-запрос
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to fetch weather data: {str(e)}"}
