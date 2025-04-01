from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# головна сторінка API
@app.route("/")
def home():
    return "Welcome to the Flask API! Visit <a href='/swagger/'>Swagger UI</a>."


# ендпоінт для отримання ресурсу (метод GET)
@app.route('/api/v1/resource', methods=['GET'])
def get_resource():
    """
    Ця функція повертає тестове повідомлення для перевірки роботи API.
    """
    return jsonify({"message": "GET-запит виконано успішно"})

# ендпоінт для створення ресурсу (метод POST)
@app.route('/api/v1/resource', methods=['POST'])
def create_resource():
    """
    Ця функція приймає JSON-дані та повертає їх у відповіді.
    """
    data = request.get_json()  # отримуємо вхідні дані у форматі JSON
    return jsonify({"message": "POST-запит виконано успішно", "data": data})

# налаштування Swagger UI для автоматичної документації API
SWAGGER_URL = "/swagger"  # URL для Swagger UI
API_URL = "/swagger.json"  # JSON-документ із описом API

# створюємо Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "My Flask API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# генерація Swagger JSON для опису API
@app.route("/swagger.json")
def swagger_json():
    """
    Ця функція генерує Swagger-документацію у форматі JSON.
    """
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "My Flask API",
            "version": "1.0.0"
        },
        "paths": {
            "/api/v1/resource": {
                "get": {
                    "summary": "Отримати ресурс",
                    "responses": {
                        "200": {"description": "Успішна відповідь"}
                    }
                },
                "post": {
                    "summary": "Створити ресурс",
                    "parameters": [
                        {
                            "in": "body",
                            "name": "body",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"}
                                }
                            }
                        }
                    ],
                    "responses": {
                        "200": {"description": "Ресурс успішно створено"}
                    }
                }
            }
        }
    })

# запуск додатку Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
