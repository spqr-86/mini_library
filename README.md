<h1 align="center">foodgram_project</h1>

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

# Описание сервиса
Мини-библиотека книг.<br>
# Установка
1. Клонируйте репрозиторий ```https://github.com/spqr-86/mini_library```
2. Создайте файл .env по примеру env.example.
3. Установите Docker (https://docs.docker.com/engine/install/)
4. Выполните ```docker-compose up -d --build```
5. Выполните:<br>
  ```docker-compose exec web python manage.py migrate --noinput```<br>
  ```docker-compose exec web python manage.py createsuperuser```<br>
  ```docker-compose exec web python manage.py collectstatic --no-input ```
6. Теперь проект доступен по адресу http://127.0.0.1:8000/

# Технологии
* Python
* Django
* Ajax
* Docker

# Проект разработал:
* [Петр Балдаев](https://github.com/spqr-86)
