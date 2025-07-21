from app.db import collection, db

def test_connection():
    print("Collections:", db.list_collection_names())
    result = collection.insert_one({"test": "connection_check"})
    print("Inserted ID:", result.inserted_id)
    doc = collection.find_one({"_id": result.inserted_id})
    print("Retrieved document:", doc)

if __name__ == "__main__":
    test_connection()
