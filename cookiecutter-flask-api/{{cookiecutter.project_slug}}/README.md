# Використання шаблону-розширення бібліотеки cookiecutter для REST API на Flask з документацією SwaggerUI

### 1. Завантажуємо наш проект з гітхабу

git clone <посилання>

### 2. Завантажуємо бібліотеку cookiecutter, яку брали за основу:

pip install cookiecutter

### 3. Генеруємо новий проєкт із шаблону

cookiecutter cookiecutter-flask-api

### 4. Програма запуститься та запропонує ввести 5 параметрів для налаштування

[1/5] project_name (My Flask API): <enter_here>
[2/5] project_slug (my_flask_api): <enter_here>
[3/5] author_name (Svitlana Denysenko): <enter_here>
[4/5] description (A simple Flask REST API with Swagger documentation): <enter_here>
[5/5] flask_port (5000): <enter_here>

### 5. Переходимо в новостворений проєкт

cd <project_name>

### 6. Встановлюємо необхідні бібліотеки з файлу залежностей

pip install -r requirements.txt

### 7. Запускаємо сервер

python app.py

##### Якщо все створено успішно, в терміналі переходимо за посиланням:

- Running on http://127.0.0.1:5000

###### (Порт визначається як один з 5 параметрів при створенні шаблону)
