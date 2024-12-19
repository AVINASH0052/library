import requests

BASE_URL = "http://127.0.0.1:5001"

# Function to login and retrieve token
def login():
    response = requests.post(f"{BASE_URL}/login", json={"username": "admin", "password": "password"})
    if response.status_code == 200:
        return response.json().get("token")
    else:
        print("Login failed:", response.json())
        return None

# Add test books
def add_test_books(token):
    headers = {"x-access-token": token}
    test_books = [
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "Moby Dick", "author": "Herman Melville"},
        {"title": "War and Peace", "author": "Leo Tolstoy"}
    ]
    for book in test_books:
        response = requests.post(f"{BASE_URL}/books", json=book, headers=headers)
        print("Add Book:", response.json())

# Add test members
def add_test_members(token):
    headers = {"x-access-token": token}
    test_members = [
        {"name": "Alice Johnson", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        {"name": "Charlie Brown", "email": "charlie@example.com"},
    ]
    for member in test_members:
        response = requests.post(f"{BASE_URL}/members", json=member, headers=headers)
        print("Add Member:", response.json())

if __name__ == "__main__":
    # Login to get the token
    token = login()
    if token:
        # Add sample books
        add_test_books(token)
        
        # Add sample members
        add_test_members(token)
