from app.db import order_collection

def save_order(order_id, order_data,email):
    return order_collection.update_one(
        {"order_id": int(order_id)},
        {"$set": {
            "order_id": order_id,
            "email":email,
            "order": order_data
        }},
        upsert=True
    )

def get_order(order_id):
    doc = order_collection.find_one(
        {"order_id": order_id},
        {"_id": 0, "order": 1}
    )
    return doc.get("order") if doc else None

def save_client_preferences(order_id, preferences,email):
    return order_collection.update_one(
        {"order_id": order_id},
        {"$set": {
            "client_preferences": preferences,
            "email":email
        }},
        upsert=True
    )


def get_client_preferences(email):
    doc = order_collection.find_one(
        {"email": email},
        {"_id": 0, "client.preferences": 1}
    )
    return doc.get("client", {}).get("preferences") if doc else None

def get_full_order_by_order_id(order_id):
   
    doc = order_collection.find_one(
        {"order_id": int(order_id)},
        {"_id": 0, "order": 1, "client_preferences": 1}  # Project only needed fields
    )
    if not doc:
        return None

    # Return combined order and client preferences as one dict
    return {
        "order": doc.get("order"),
        "preferences": doc.get("client_preferences")
    }
def get_all_orders_by_email(email):
    cursor = order_collection.find(
        {"email": email},
        {"_id": 0, "order_id": 1, "order": 1, "client_preferences": 1}
    )
    return [
        {
            "order_id": doc.get("order_id"),
            "order": doc.get("order"),
            "preferences": doc.get("client_preferences")  # now will return real value
        }
        for doc in cursor
    ]

