from fastapi import FastAPI
from app.routes import weather, auth
from app.database import Base, engine

app = FastAPI(
    title="Weather API",
    description="REST API with FastAPI and OpenWeatherMap",
    version="1.0.0"
)

# Подключаем маршруты
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the Weather API!"}

# Создаем таблицы
Base.metadata.create_all(bind=engine)
