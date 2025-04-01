#!/usr/bin/env python
import os
import subprocess
import sys
import time
import platform

# Визначення операційної системи
IS_WINDOWS = platform.system() == "Windows"

# Параметри з cookiecutter.json
git_integration = "{{cookiecutter.git_integration}}"
git_username = "{{cookiecutter.git_username}}"
git_token = "{{cookiecutter.git_token}}"
git_private_repo = "{{cookiecutter.git_private_repo}}" == "yes"
install_dependencies = "{{cookiecutter.install_dependencies}}" == "yes"
code_style = "{{cookiecutter.code_style}}"
project_name = "{{cookiecutter.project_name}}"
project_slug = "{{cookiecutter.project_slug}}"
project_description = "{{cookiecutter.project_description}}"


def execute_command(command, error_message="Помилка виконання команди"):
    """Виконати команду та вивести повідомлення про помилку за необхідності"""
    try:
        # Для команд pip в Windows використовуємо модуль python -m pip
        if IS_WINDOWS and command.startswith("pip "):
            command = command.replace("pip ", "python -m pip ")

        subprocess.check_call(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        print(f"{error_message}: {command}")
        return False


def initialize_git():
    """Ініціалізувати локальний Git репозиторій"""
    print("Ініціалізація Git репозиторія...")
    execute_command("git init", "Помилка при ініціалізації Git")
    execute_command("git add .", "Помилка при додаванні файлів в Git")
    execute_command('git commit -m "Initial commit"', "Помилка при виконанні першого коміту")

    # Налаштування назви гілки (в нових версіях Git використовується main)
    execute_command('git branch -M main', "Помилка при перейменуванні гілки")

    return True


def create_github_repo():
    """Створити репозиторій на GitHub та надіслати код"""
    try:
        from github import Github

        print("Створення GitHub репозиторія...")
        # Авторизація в GitHub
        g = Github(git_token)
        user = g.get_user()

        # Створення репозиторія
        repo = user.create_repo(
            project_slug,
            description=project_description,
            private=git_private_repo
        )

        # Додавання віддаленого репозиторія та відправка коду
        remote_url = f"https://{git_username}:{git_token}@github.com/{git_username}/{project_slug}.git"
        execute_command(f'git remote add origin {remote_url}', "Помилка при додаванні віддаленого репозиторія")
        execute_command('git push -u origin main', "Помилка при відправці коду в GitHub")

        print(f"GitHub репозиторій створено: {repo.html_url}")
        return True
    except ImportError:
        print("Помилка: Не встановлена бібліотека PyGithub. Встановіть її за допомогою 'pip install PyGithub'")
        return False
    except Exception as e:
        print(f"Помилка при створенні GitHub репозиторія: {str(e)}")
        return False


def create_gitlab_repo():
    """Створити репозиторій на GitLab та надіслати код"""
    try:
        import gitlab

        print("Створення GitLab репозиторія...")
        # Авторизація в GitLab
        gl = gitlab.Gitlab('https://gitlab.com', private_token=git_token)
        gl.auth()

        # Створення репозиторія
        project = gl.projects.create({
            'name': project_name,
            'description': project_description,
            'visibility': 'private' if git_private_repo else 'public'
        })

        # Додавання віддаленого репозиторія та відправка коду
        remote_url = f"https://oauth2:{git_token}@gitlab.com/{git_username}/{project_slug}.git"
        execute_command(f'git remote add origin {remote_url}', "Помилка при додаванні віддаленого репозиторія")
        execute_command('git push -u origin main', "Помилка при відправці коду в GitLab")

        print(f"GitLab репозиторій створено: {project.web_url}")
        return True
    except ImportError:
        print("Помилка: Не встановлена бібліотека python-gitlab. Встановіть її за допомогою 'pip install python-gitlab'")
        return False
    except Exception as e:
        print(f"Помилка при створенні GitLab репозиторія: {str(e)}")
        return False


def setup_code_style():
    """Налаштувати обраний стиль кодування"""
    if code_style == "black":
        print("Налаштування Black для форматування коду...")
        execute_command("pip install black", "Помилка при встановленні Black")
        # Форматування коду за допомогою Black
        execute_command("black .", "Помилка при форматуванні коду за допомогою Black")

        # Створення pre-commit hook для Black
        with open(".git/hooks/pre-commit", "w") as f:
            f.write("""#!/bin/sh
# Форматування коду за допомогою Black перед комітом
black .
""")
        # Платформно-залежна команда для налаштування прав
        if IS_WINDOWS:
            print("Пропуск налаштування прав для pre-commit на Windows")
        else:
            execute_command("chmod +x .git/hooks/pre-commit", "Помилка при налаштуванні pre-commit hook")

    elif code_style == "flake8":
        print("Налаштування Flake8 для перевірки стилю коду...")
        execute_command("pip install flake8", "Помилка при встановленні Flake8")

        # Створення pre-commit hook для Flake8
        with open(".git/hooks/pre-commit", "w") as f:
            f.write("""#!/bin/sh
# Перевірка стилю коду за допомогою Flake8 перед комітом
flake8 .
if [ $? -ne 0 ]; then
    echo "Помилки стилю коду! Виправте їх перед комітом."
    exit 1
fi
""")
        # Платформно-залежна команда для налаштування прав
        if IS_WINDOWS:
            print("Пропуск налаштування прав для pre-commit на Windows")
        else:
            execute_command("chmod +x .git/hooks/pre-commit", "Помилка при налаштуванні pre-commit hook")


def install_project_dependencies():
    """Встановити залежності проекту з requirements.txt"""
    if os.path.exists("requirements.txt"):
        print("Встановлення залежностей проекту...")
        execute_command("pip install -r requirements.txt", "Помилка при встановленні залежностей")


def main():
    """Головна функція, що виконує всі налаштування після генерації проекту"""
    # Ініціалізація Git
    if git_integration != "none":
        init_success = initialize_git()
        if not init_success:
            print("Не вдалося ініціалізувати Git. Пропуск інтеграції з GitHub/GitLab.")
            return

        # Створення віддаленого репозиторія
        if git_integration == "github":
            create_github_repo()
        elif git_integration == "gitlab":
            create_gitlab_repo()

    # Налаштування стилю кодування
    if code_style != "none":
        setup_code_style()

    # Встановлення залежностей проекту
    if install_dependencies:
        install_project_dependencies()

    print("\nПроект успішно налаштовано!")
    print(f"Директорія проекту: {os.getcwd()}")


if __name__ == "__main__":
    main()
