from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def generate_password(length: int) -> str:
    """
    Generate a secure password with a mix of lowercase, uppercase, and numbers.
    """
    if length < 3:
        length = 3  # Ensure minimum length of 3

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = "".join(random.choice(alphabet) for _ in range(length))

    password = replace_with_number(password)
    password = replace_with_uppercase_letter(password)

    return password


def replace_with_number(password: str) -> str:
    """
    Replace a random character in the first half of the password with a number.
    """
    for _ in range(random.randint(1, 2)):
        index = random.randint(0, len(password) // 2 - 1)
        password = password[:index] + str(random.randint(0, 9)) + password[index + 1:]
    return password


def replace_with_uppercase_letter(password: str) -> str:
    """
    Replace a random character in the second half of the password with an uppercase letter.
    """
    for _ in range(random.randint(1, 2)):
        index = random.randint(len(password) // 2, len(password) - 1)
        password = password[:index] + password[index].upper() + password[index + 1:]
    return password


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        num_passwords = int(data.get('num_passwords', 1))
        length = int(data.get('length', 8))

        if num_passwords < 1 or length < 3:
            return jsonify({"error": "Invalid input values"}), 400

        passwords = [generate_password(length) for _ in range(num_passwords)]
        return jsonify({"passwords": passwords})

    except ValueError:
        return jsonify({"error": "Invalid input format"}), 400


if __name__ == '__main__':
    app.run(debug=True)
