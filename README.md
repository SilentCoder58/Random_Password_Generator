# Flask Password Generator

This is a simple Flask-based password generator web application. Users can specify the number and length of passwords to generate, and the application will return randomized passwords with a mix of lowercase, uppercase, and numbers.

## Features
- Web-based interface using Flask
- Secure random password generation
- Dynamic password generation via API
- Responsive UI with HTML, CSS, and JavaScript

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SilentCoder58/flask-password-generator.git
   cd flask-password-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoint
- `POST /generate`
  - **Request Body (JSON):**
    ```json
    {
      "num_passwords": 3,
      "length": 10
    }
    ```
  - **Response (JSON):**
    ```json
    {
      "passwords": ["A1bcD3efgh", "Z9xyW2klmn", "R8stU4opqr"]
    }
    ```

## Project Structure
```
flask_password_generator/
│── app.py  # Flask main app
│── templates/
│   ├── index.html  # Frontend UI
│── static/
│   ├── style.css  # Styles
│   ├── script.js  # JavaScript logic
```

