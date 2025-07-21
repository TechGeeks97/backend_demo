from app.db import collection

def save_user_profile(email, profile_data):
    return collection.update_one(
        {"email": email},
        {"$set": {
            "email": email,
            "name": profile_data.get("name"),
            "age": profile_data.get("age"),
            "occupation": profile_data.get("occupation")
        }},
        upsert=True
    )

def get_user_profile(email):
    doc = collection.find_one(
        {"email": email},
        {"_id": 0}  # exclude _id, include all other fields
    )
    return doc
def save_learning_goals(email, goals):
    return collection.update_one(
        {"email": email},
        {"$set": {"learning.goals": goals}},
        upsert=True
    )

def get_learning_goals(email):
    doc = collection.find_one(
        {"email": email},
        {"_id": 0, "learning.goals": 1}
    )
    return doc.get("learning", {}).get("goals") if doc else None

def save_feedback(email, feedback):
    return collection.update_one(
        {"email": email},
        {"$set": {"feedback.text": feedback}},
        upsert=True
    )

def get_feedback(email):
    doc = collection.find_one(
        {"email": email},
        {"_id": 0, "feedback.text": 1}
    )
    return doc.get("feedback", {}).get("text") if doc else None

def get_full_user_context(email):
    data = get_user_profile(email)


    return  data

