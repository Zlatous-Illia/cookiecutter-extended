## Залежності, які потрібно встановити для роботи з шаблоном:

```bash
pip install cookiecutter  # для встановлення cookiecutter
pip install PyGithub      # для роботи з GitHub API
pip install python-gitlab # для роботи з GitLab API

```

## У кореневій папці, де знаходиться проект із шаблоном, виконайте команду:

```bash
python -m cookiecutter .\cookiecutter-github-api\
```

Для створення проекту за допомогою шаблону необхідний токен:<br>
https://github.com/settings/tokens/new

У вікні створення токена потрібно вказати назву токена, вибрати термін дії токена та вказати права доступу (вибрати пункт repo).

Після генерації токена необхідно його скопіювати.