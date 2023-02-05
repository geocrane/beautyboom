<h1 align="center">Интернет-магазин BeautyBoom</h1>

<p align="center"><img src="https://img.shields.io/badge/made%20by-geocrane-green">
<img src=https://img.shields.io/badge/Python-%203.7-blue>
<img src=https://img.shields.io/badge/Django-%203.2.16-red>
</p>
<h1 align="center"></h1>

**(в разработке)**
Интернет-магазин товаров для специалистов в сфере услуг красоты.

Требуется реализовать:
- каталог товаров с возможностью администрирования
- разделение товаров по группам и подгруппам
- функция добавления товара в избранное
- функция добавления товара в корзину
- оформление заказа для доставки

## Используется:
- Python 3.7
- Django 3.2.16
- SQLite 3 (с заменой на PostgreSQL)
- free-шаблон HTML/CSS/JS

## Запуск (на примере Linux): 
Cклонируйте репозиторий на локальный пк:
```
git clone https://github.com/geocrane/beautyboom.git
```
Войдите в склонированный репозиторий.
Для запуска на локальном сервере поочередно выполните:
```
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

cd beautyboom

python3 manage.py migrate

python3 manage.py runserver
```

Приложение доступно по адресу:
```
http://127.0.0.1:8000/
```

Заполнение БД случайными категориями и товарами:
```
python3 manage.py generate_data
```

<p></p>
<h3 align="center">developed by: Sergey S. Zhuravlev</h5>
