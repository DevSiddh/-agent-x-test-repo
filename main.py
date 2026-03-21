def get_user(user_id):
    database = {"1": {"name": "Alice"}}
    return database.get(user_id) # Returns None for "2"

user = get_user("2")
print(f"User name: {user.name}") # AttributeError: 'NoneType' object has no attribute 'name'
