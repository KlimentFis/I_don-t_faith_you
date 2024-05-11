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
Для использования по прямому назначению:
```shell
python manage.py runserver 0.0.0.0:8888
```
## Руководство по Rest API
### id  - целое число, передаваемое на прямую
- ### GET api/change_naeb/id - Для инвертирования статуса проекта, с переданным id 
- ### POST /api/is_naeb/id - Для создания проекта, по пераданным значениям
Пример входного JSON:
```json
{
    "name": "Название проекта",
    "is_naeb": false
}
```
- ### GET /api/is_naeb/id - Возврат статуса нужного проекта
- ### GET /api/all_projects/ - Для возврата всех проектов, и их статусов
