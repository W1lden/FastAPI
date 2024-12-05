FastAPI Weather Service

Этот проект предоставляет REST API для получения данных о погоде через интеграцию с OpenWeather API.

Локальный запуск

Клонируйте репозиторий:
git clone https://github.com/W1lden/FastAPI.git
cd FastAPI
Создайте виртуальное окружение и активируйте его:
python -m venv .venv
source .venv/bin/activate  # Для Linux/Mac
.venv\Scripts\activate     # Для Windows
Установите зависимости:
pip install -r requirements.txt
Создайте файл .env для хранения ключа OpenWeather API:
OPENWEATHER_API_KEY=ваш_ключ_API
Запустите приложение:
uvicorn app.main:app --reload
Откройте Swagger-документацию:
URL: http://127.0.0.1:8000/docs
Эндпоинты и примеры запросов

Авторизация
1. Получение токена:

POST /auth/token

Запрос:

curl -X POST "http://127.0.0.1:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=user&password=password"
Пример ответа:

{
    "access_token": "ваш_jwt_token",
    "token_type": "bearer"
}
Эндпоинты погоды
2. Создание записи о погоде:

POST /weather/

Запрос:

curl -X POST "http://127.0.0.1:8000/weather/" \
-H "Authorization: Bearer ваш_jwt_token" \
-H "Content-Type: application/json" \
-d '{"city": "London"}'
Пример ответа:

{
    "city": "London",
    "temperature": 15.5,
    "description": "clear sky",
    "datetime": "2024-12-05T12:00:00"
}
3. Получение последней записи о погоде:

GET /weather/{city}

Запрос:

curl -X GET "http://127.0.0.1:8000/weather/London" \
-H "Authorization: Bearer ваш_jwt_token"
Пример ответа:

{
    "city": "London",
    "temperature": 15.5,
    "description": "clear sky",
    "datetime": "2024-12-05T12:00:00"
}
