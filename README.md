# where_to_go
 Проект на библиотеке [Django](https://www.djangoproject.com/), созданный для нахождения просмотра красивых мест в москве и московской области, и их размещения.
 
 Сайт доступен по этому [адресу](https://ykyki4.pythonanywhere.com/), здесь хранится 20 разных локаций, но вы можете добавить свои!
 
 ## Способ №1, добавление через админку
 
 Для начала, скачайет репозиторий в .zip или клонируйте его, изолируйте проект с помощью venv, установите зависимости командой:
 ```
 pip install -r requirements.txt
 ```
 
 Далее, создайте файл .env и установите следующие переменные окружения:
 
 * [DEBUG](https://docs.djangoproject.com/en/4.1/ref/settings/#debug)
 * [ALLOWED_HOSTS](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts)
 * [SECURE_SSL_REDIRECT](https://docs.djangoproject.com/en/4.1/ref/settings/#secure-ssl-redirect)
 * [SESSION_COOKIE_SECURE](https://docs.djangoproject.com/en/4.1/ref/settings/#session-cookie-secure)
 * [CSRF_COOKIE_SECURE](https://docs.djangoproject.com/en/4.1/ref/settings/#csrf-cookie-secure)
 * [SECRET_KEY](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key)
 * [STATIC_URL](https://docs.djangoproject.com/en/4.1/ref/settings/#static-url)
 * [STATICFILES_DIRS](https://docs.djangoproject.com/en/4.1/ref/settings/#staticfiles-dirs)
 * [MEDIA_URL](https://docs.djangoproject.com/en/4.1/ref/settings/#media-url)

Когда справились с предыдущем шагом, вам надо запустить ряд команд в терминал

Создайте базу данных:

```
 python manage.py migrate
```

Создайте администратора:
```
 python manage.py createsuperuser
```

Запустите сервер локально:
```
 python manage.py runserver
```
 
После этого, сервер будет доступен по ссылке http://127.0.0.1:8000

Для админки, откройте http://127.0.0.1:8000/admin, зайдите в созданный только что аккаунт, и добавляйте места вместе с картинками!

## Способ №2 добавление через json

Вам потребует всё, что было в предыдущем способе, кроме админки. 
Вместо неё, нужна команда:

```
 python manage.py load_place {ссылка на json}
```

json должен быть такого формата:

```
{
    "title": {Название локации},
    "imgs": [
        {Cсылка на картинку},
        ...
        {Cсылка на картинку},
    ],
    "description_short": {Краткое описание локации},
    "description_long": {Полное описание локации с HTML-форматированием},
    "coordinates": {
        "lng": {Долгота в  градусах},
        "lat": {Широта в градусах}
    }
}
```
