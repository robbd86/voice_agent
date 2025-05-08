import requests, os

def get_weather(location):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    return {
        "location": location,
        "temperature": res["main"]["temp"],
        "description": res["weather"][0]["description"]
    }