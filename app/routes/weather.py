from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Weather
from app.schemas import WeatherCreate, WeatherResponse
from fastapi.security import OAuth2PasswordBearer
from app.routes.auth import verify_token
from app.services.weather import OpenWeatherService  # Подключаем новый сервис

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=WeatherResponse)
def create_weather_record(request: WeatherCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Проверяем токен
    verify_token(token)

    # Получаем данные через OpenWeatherService
    weather_data = OpenWeatherService.get_weather(request.city)
    if "error" in weather_data:
        raise HTTPException(status_code=400, detail=weather_data["error"])
    
    # Извлекаем данные из ответа
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    # Сохраняем в базу данных
    weather_record = Weather(city=city, temperature=temperature, description=description)
    db.add(weather_record)
    db.commit()
    db.refresh(weather_record)
    return weather_record

@router.get("/{city}", response_model=WeatherResponse)
def get_weather_record(city: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Проверяем токен
    verify_token(token)

    # Ищем данные в базе
    weather_record = db.query(Weather).filter(Weather.city == city).order_by(Weather.datetime.desc()).first()
    if not weather_record:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return weather_record
