from pydantic import BaseModel
from datetime import datetime

class WeatherCreate(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    datetime: datetime

    class Config:
        orm_mode = True
