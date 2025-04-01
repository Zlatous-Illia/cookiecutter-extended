#!/usr/bin/env python
import os
import shutil

# Отримуємо значення змінних із cookiecutter.json
include_docker = "{{ cookiecutter.include_docker }}" == "yes"
include_docker_compose = "{{ cookiecutter.include_docker_compose }}" == "yes"
include_dockerignore = "{{ cookiecutter.include_dockerignore }}" == "yes"

# Видаляємо Dockerfile, якщо він не потрібний
if not include_docker:
    dockerfile_path = os.path.join(os.getcwd(), "Dockerfile")
    if os.path.exists(dockerfile_path):
        os.remove(dockerfile_path)
        print("Видалено Dockerfile, тому що опція include_docker = no")

# Видаляємо docker-compose.yml, якщо він не потрібний
if not include_docker_compose:
    docker_compose_path = os.path.join(os.getcwd(), "docker-compose.yml")
    if os.path.exists(docker_compose_path):
        os.remove(docker_compose_path)
        print("Видалено docker-compose.yml, так як опція include_docker_compose = no")

# Видаляємо .dockerignore, якщо він не потрібен
if not include_dockerignore:
    dockerignore_path = os.path.join(os.getcwd(), ".dockerignore")
    if os.path.exists(dockerignore_path):
        os.remove(dockerignore_path)
        print("Видалено .dockerignore, так як опція include_dockerignore = no")

# Виводимо інформацію про створене Docker-оточення
if include_docker:
    print("Створено Dockerfile для проекту")

    if include_docker_compose:
        print("Створено docker-compose.yml для проекту")
        services = "{{ cookiecutter.docker_compose_services }}"
        if services != "none":
            print(f"  Налаштовані сервіси: {services}")

    if include_dockerignore:
        print("Створено .dockerignore для проекту")

    print("\nДля сборки та запуску Docker-контейнера використовуйте:")
    print("   docker build -t {{ cookiecutter.project_slug }} .")
    print(
        "   docker run -p {{ cookiecutter.docker_expose_port }}:{{ cookiecutter.docker_expose_port }} {{ cookiecutter.project_slug }}")

    if include_docker_compose:
        print("\nАбо використовуйте docker-compose:")
        print("   docker-compose up --build")