# AddressStandardizerAPI

_API для стандартизации адресов с использованием сервиса Dadata._

## Установка и настройка

1. Клонируйте репозиторий: `git@github.com:MrSunstrike/AddressStandardizerAPI.git` на ваше устройство.
2. Cоздайте виртуальное окружение и установите зависимости: `pip install -r requirements.txt`
3. Создайте файл `.env` в корневой директории проекта и задайте значения переменных окружения:
    - `SECRET_KEY` - секретный ключ приложения Django для файла `settings.py`. Установите любую комбинацию.
    - `API_KEY_DADATA` - API ключ сервиса DADATA. Получить можно после регистрации на https://dadata.ru/
    - `SECRET_KEY_DADATA` - API ключ сервиса DADATA. Получить можно после регистрации на https://dadata.ru/
4. Выполнить миграции базы данных: `python manage.py migrate`
5. Запустите сервер разработки: `python manage.py runserver`

## Использование API

### Эндпоинт

- `POST /v1/address/`

### Параметры запроса

- `request` (строка): Адрес для стандартизации.

### Пример запроса

```
POST /v1/address/
Content-Type: application/json

{
  "request": "мск сухонска 11/-89"
}
```

### Пример ответа

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "request": "мск сухонска 11/-89",
  "result": "г Москва, ул Сухонская, д 11, кв 89"
}
```

## Лицензия

Проект лицензирован в соответствии с лицензией [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

## Автор

Автор проекта - Mr.Sunstrike

  - Email: misha@mrsunstrike.ru
  - GitHub: [github.com/MrSunstrike](https://github.com/MrSunstrike)