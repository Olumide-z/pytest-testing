import requests
database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "David",
    5: "Eve",
    6: "Faythe",
    7: "Grace",
    8: "Heidi",
    9: "Judy",
    10: "Mallory",
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_user_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
