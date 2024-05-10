# Не наебешь!!!

## Цель проекта
Создать Rest API, для того чтобы блокировать мобильное приложение, в случае недобросовестности заказчика.

## Установка

Клонирование проекта:
```shell
git clone https://github.com/KlimentFis/I_don-t_faith_you 
```

Переход в папку проекта:
```shell
cd I_don-t_faith_you
```

Установка и активация виртуального окружения ( Не обязательно ):
```shell
python -m venv venv && venv\Scripts\activate.bat
```

Установка зависимостей:
```shell
pip install -r requirements.txt
```

Создание миграций:
```shell
python manage.py makemigrations
```

Проведение миграций:
```shell
python manage.py migrate
```

Создание Супер-пользователя ( Не обязательно ):
```shell
python manage.py createsuperuser
```

## Запуск проекта
Для локальной разработки:
```shell
python manage.py runserver
```
