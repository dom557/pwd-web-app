from flask import Flask, render_template, request, jsonify
from generator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form.get('length', 10))
    uppercase = 'uppercase' in request.form
    lowercase = 'lowercase' in request.form
    digits = 'digits' in request.form
    special = 'special' in request.form

    if not any([uppercase, lowercase, digits, special]):
        lowercase = True  # Set lowercase as default if none chosen

    password = generate_password(length, uppercase, lowercase, digits, special)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
