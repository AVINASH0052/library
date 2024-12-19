from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secretkey'

books = []
members = []
token_validity_minutes = 30

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.secret_key, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if auth and auth.get('username') == 'admin' and auth.get('password') == 'password':
        token = jwt.encode({'user': auth['username'],
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=token_validity_minutes)},
                           app.secret_key, algorithm="HS256")
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.json
    book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    return jsonify({'message': 'Book added successfully!', 'book': book})

@app.route('/books', methods=['GET'])
@token_required
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    
    filtered_books = books
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]
    
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = filtered_books[start:end]

    return jsonify({'books': paginated_books, 'total': len(filtered_books)})

@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    data = request.json
    for book in books:
        if book['id'] == book_id:
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            return jsonify({'message': 'Book updated successfully!', 'book': book})
    return jsonify({'message': 'Book not found!'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully!'})

@app.route('/members', methods=['POST'])
@token_required
def add_member():
    data = request.json
    member = {
        'id': len(members) + 1,
        'name': data['name'],
        'email': data['email']
    }
    members.append(member)
    return jsonify({'message': 'Member added successfully!', 'member': member})

@app.route('/members', methods=['GET'])
@token_required
def get_members():
    return jsonify({'members': members})

@app.route('/members/<int:member_id>', methods=['PUT'])
@token_required
def update_member(member_id):
    data = request.json
    for member in members:
        if member['id'] == member_id:
            member['name'] = data.get('name', member['name'])
            member['email'] = data.get('email', member['email'])
            return jsonify({'message': 'Member updated successfully!', 'member': member})
    return jsonify({'message': 'Member not found!'}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
@token_required
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return jsonify({'message': 'Member deleted successfully!'})

@app.route('/')
def home():
    return "<h1>Welcome to the Library Management System API</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
