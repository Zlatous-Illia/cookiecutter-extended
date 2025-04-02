{% if cookiecutter.include_docker == "yes" %}
FROM {{ cookiecutter.docker_base_image }}

WORKDIR /app

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта
COPY . .

# Порт, который будет слушать приложение
EXPOSE {{ cookiecutter.docker_expose_port }}

# Запуск приложения
CMD ["python", "app.py"]
{% endif %}