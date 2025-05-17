import requests, os

def get_weather(location):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    res = requests.get(url)
    try:
        data = res.json()
        if res.status_code != 200:
            return {"error": data.get("message", "Failed to fetch weather data")}
        return {
            "location": location,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except Exception as e:
        return {"error": str(e)}