```markdown
   # {{ cookiecutter.project_name }}

   {{ cookiecutter.project_description }}

   ## Автор

   {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})

   ## Як запустити проект

   {% if cookiecutter.include_docker == "yes" %}
   ### З використанням Docker

   Зберіть та запустіть Docker-контейнер:

   ```bash
   docker build -t {{ cookiecutter.project_slug }} .
   docker run -p {{ cookiecutter.docker_expose_port }}:{{ cookiecutter.docker_expose_port }} {{ cookiecutter.project_slug }}
   ```

   {% if cookiecutter.include_docker_compose == "yes" %}
   ### З використанням Docker Compose

   ```bash
   docker-compose up --build
   ```
   {% endif %}
   {% endif %}

   ### Без Docker

   ```bash
   pip install -r requirements.txt
   python app.py
   ```
   ```

