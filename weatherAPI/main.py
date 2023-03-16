from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()    

api_key = "d92e96408b96717b6a7e5e88a2c987e0"

@app.get("/{city}")
def weather(city: str):
    data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")

    sky = data.json()["weather"][0]["main"]
    temperature = round(data.json()["main"]["temp"])
    temperature_min = round(data.json()["main"]["temp_min"])
    temperature_max = round(data.json()["main"]["temp_max"])

    return {f"Details about {city.capitalize()}": (f"Sky: {sky}", 
                        f"Temperature: {temperature} º Celsius", 
                        f"Min Temperature: {temperature_min} º Celsius", 
                        f"Max Temperature: {temperature_max} º Celsius")}