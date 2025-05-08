from datetime import datetime
import pytz

def get_time(location):
    # Map common city names to pytz timezones
    city_to_timezone = {
        "tokyo": "Asia/Tokyo",
        "new york": "America/New_York",
        "london": "Europe/London",
        "paris": "Europe/Paris",
        "sydney": "Australia/Sydney",
        "los angeles": "America/Los_Angeles",
        # Add more as needed
    }
    try:
        tz_name = city_to_timezone.get(location.strip().lower(), location)
        tz = pytz.timezone(tz_name)
        now = datetime.now(tz)
        return {"location": location, "current_time": now.strftime("%Y-%m-%d %H:%M:%S")}
    except Exception:
        return {"error": "Invalid timezone"}