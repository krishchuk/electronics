## Electronics

### Модель сети по продаже электроники

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-464646?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)


### Технологии:
- python 3.12
- django 5.1
- DRF 3.15.2
- PostgreSQL


### Установка и запуск проекта:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/krishchuk/electronics.git
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Настройте переменные окружения в файле `.env` по примеру из `.env.sample`:
    ```
    SECRET_KEY=your-secret-key
    ...
    ```
4. Выполните миграции:
    ```bash
    python manage.py migrate
    ```
5. Загрузите фикстуры с данными:
    ```bash
    python manage.py loaddata имя_фикстуры.json
    ```
6. Создайте суперпользователя:
    ```bash
    python manage.py csu
    ```
7. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```
8. Приложение доступно по адресу http://127.0.0.1:8000/.


### Автор проекта:
https://github.com/krishchuk/