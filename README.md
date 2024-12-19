# Library Management System API

This project provides a RESTful API for a Library Management System, built using Flask. The API supports authentication, CRUD operations for books and members, and optional filtering and pagination for books.

## How to Run the Project

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:AVINASH0052/library.git
   cd <repository-folder>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # For macOS/Linux
   .\env\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install flask pyjwt
   ```

4. Start the Flask server:
   ```bash
   python main.py
   ```

5. The server will run at `http://127.0.0.1:5001`. Use tools like `curl`, Postman, or the provided `test.py` script to interact with the API.

### Testing the API
1. Run the test script to populate the API with sample data:
   ```bash
   python test.py
   ```
2. Access endpoints via Postman or a browser:
   - Root URL: `http://127.0.0.1:5001/`
   - View Books: `http://127.0.0.1:5001/books`
   - View Members: `http://127.0.0.1:5001/members`

## Design Choices

### Authentication
- Token-based authentication ensures secure access to protected endpoints.
- JWTs are generated upon login and validated for each request.

### Data Management
- In-memory data storage is used for simplicity. Each session resets the data.
- Lists (`books` and `members`) serve as the storage mechanism.

### API Design
- CRUD endpoints for both books and members follow REST principles.
- Query parameters allow filtering and pagination for books.

### Assumptions
- Admin credentials (`username: admin`, `password: password`) are hardcoded for demonstration purposes.
- Books and members are stored in memory, making the API stateless.
- The API does not include advanced error handling for production environments.

## Limitations
- Data Persistence: Since the data is stored in memory, it will reset when the server restarts.
- Security: The secret key is static and not stored securely.
- Scalability: In-memory storage is not suitable for large-scale applications.
- Validation: Input data validation is minimal.

## Future Improvements
- Integrate a database for persistent storage.
- Add robust error handling and input validation.
- Implement logging and monitoring for production readiness.
- Enhance authentication by using environment variables for sensitive information.

