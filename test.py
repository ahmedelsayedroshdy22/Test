import requests

# Create a user
response = requests.post("http://127.0.0.1:8000/users", json={
    "name": "Ahmed",
    "email": "ahmed@test.com"
})
print("Created:", response.json())

# Get all users
response = requests.get("http://127.0.0.1:8000/users")
print("All users:", response.json())
