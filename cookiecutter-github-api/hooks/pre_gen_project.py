#!/usr/bin/env python
import re
import sys

# Перевірка коректності імені проєкту
project_slug = "{{cookiecutter.project_slug}}"
if not re.match(r'^[a-z][a-z0-9_]+$', project_slug):
    print(f"ПОМИЛКА: {project_slug} - некоректне ім'я проєкту. Використовуйте тільки малі літери, цифри та підкреслення.")
    sys.exit(1)

# Перевірка токена для GitHub/GitLab
git_integration = "{{cookiecutter.git_integration}}"
git_token = "{{cookiecutter.git_token}}"

if git_integration != "none" and not git_token:
    print("ПОМИЛКА: Ви обрали інтеграцію з Git, але не вказали токен API.")
    sys.exit(1)