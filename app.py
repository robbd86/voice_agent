from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv
import os
from weather import get_weather
from time_api import get_time
from search import search_wikipedia

load_dotenv()

app = FastAPI()
API_KEYS = os.getenv("ALLOWED_API_KEYS", "").split(",")

@app.middleware("http")
async def log_all_requests(request, call_next):
    print(f"\U0001F4E5 Middleware Log: {request.method} {request.url}")
    response = await call_next(request)
    return response

def validate_api_key(key: str):
    if key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.post("/weather")
async def weather_endpoint(payload: dict):
    api_key = payload.get("api_key")
    validate_api_key(api_key)
    location = payload.get("location")
    return get_weather(location)


@app.post("/time")
async def time_endpoint(payload: dict):
    api_key = payload.get("api_key")
    validate_api_key(api_key)
    location = payload.get("location")
    return get_time(location)


@app.post("/search")
async def search_endpoint(payload: dict):
    print("🔍 Incoming /search payload:", payload)
    api_key = payload.get("api_key")
    validate_api_key(api_key)
    query = payload.get("query")
    return search_wikipedia(query)

