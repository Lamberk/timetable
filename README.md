# timetable

Устанавливаем pip, virtualenv, postgresql:
```
sudo apt-get install pip
sudo apt-get install virtualenv
apt-get install postgresql-9.4
```
Создаем дирикторию для проекта:
```
mkdir project
```

Заходим в созданную папку и создаем virtualenv:
```
virtualenv project_venv
```
Активируем virtualenv:
```
source project_venv/bin/activate
```
Клонируем проект:
https:
https://github.com/Lamberk/timetable.git
ssh:
git@github.com:Lamberk/timetable.git
<br>
Устанавливаем необходимые пакет:
```
pip install -r requirements.txt
```
Настраиваем базу, создаем superuser для админки Django
<br>
Заполняем базу основными данными:
```
python manage.py loaddata dumpdata.json
python manage.py generate
```
Запускаем сервер
```
python manage.py runserver
```
и тестируем приложение по адресу: localhost:8000/trainstable/search/
