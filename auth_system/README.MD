## Запуск проекта

Клонировать репозиторий:

git clone https://github.com/username/auth_test_assignment.git
cd auth_test_assignment


Создать виртуальное окружение и установить зависимости:

python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt


Настроить базу данных:

Создать Postgres DB и пользователя



Подставить свои данные БД и SECRET_KEY

Сделать миграции:

python manage.py makemigrations
python manage.py migrate


Заполнить тестовые данные через shell:

python manage.py shell


Запустить сервер:

python manage.py runserver