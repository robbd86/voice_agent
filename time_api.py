from datetime import datetime
import pytz

def get_time(location):
    try:
        tz = pytz.timezone(location)
        now = datetime.now(tz)
        return {"location": location, "current_time": now.strftime("%Y-%m-%d %H:%M:%S")}
    except:
        return {"error": "Invalid timezone"}