import json

file_path = 'adbms/mobile.json'
with open(file_path, 'r') as file:
    data = json.load(file)

if "users" in data:
    users_data = data["users"]

    # Iterate over all users
    for user_id, user_info in users_data.items():
        # Display user information
        print(f"User ID: {user_id}")
        print(f"Name: {user_info['name']}")
        print(f"Email: {user_info['email']}")
        print(f"Phone: {user_info['phone']}")

        # Display address details
        address = user_info.get('address', {})
        print("Address:")
        print(f"  Street: {address.get('street', 'N/A')}")
        print(f"  City: {address.get('city', 'N/A')}")
        print(f"  State: {address.get('state', 'N/A')}")
        print(f"  ZIP: {address.get('zip', 'N/A')}")

        # Check if the user is active
        is_active = user_info.get('is_active', False)
        print(f"Active Status: {'Active' if is_active else 'Inactive'}")

        print("-----------------------------")

else:
    print("No user data found in the JSON file.")
