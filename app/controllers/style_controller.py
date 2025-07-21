from app.db import user_style_collection

def save_style(email, style_data):
    return user_style_collection.update_one(
        {"email": email},
        {"$set": {"style": style_data}},
        upsert=True
    )

def save_weather(email, weather_data):
    return user_style_collection.update_one(
        {"email": email},
        {"$set": {"weather": weather_data}},
        upsert=True
    )

def save_occasion(email, occasion_data):
    return user_style_collection.update_one(
        {"email": email},
        {"$set": {"occasion": occasion_data}},
        upsert=True
    )

def get_user_style_profile(email):
    doc = user_style_collection.find_one(
        {"email": email},
        {
            "_id": 0,
            "style": 1,
            "weather": 1,
            "occasion": 1
        }
    )

    if not doc:
        return None

    return {
        "email": email,
        "style_profile": {
            "style": doc.get("style"),
            "weather": doc.get("weather"),
            "occasion": doc.get("occasion")
        }
    }
