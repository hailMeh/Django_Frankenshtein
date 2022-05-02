ЧАСТЬ 1 - НАЧАЛЬНАЯ УСТАНОВКА
----------------------------------------------------------------
1. Создается проект и application
2. Для Postgre устанавливается адаптер базы данных -> pip install psycopg2-binary
3. В корне создаются два файла для докера - Dockerfile и docker-compose.yml
4. Сервер останавливается и запускается консоль - > в корень проекта -> docker-compose up -d(для сохранения возможности работы при включенном сервере) --build(сразу в одну строку и build контейнера)
5. В проекте в settings устанавливается database PostgreSQL
6. Изначальная установка проекта + докер + база данных настроены.

----------------------------------------------------------------
ЧАСТЬ 2 - ИЗМЕНЕНИЕ стандратной модели юзера Джанго
-----------------------------------------------------------------
Создаем новый app для аккаунтов юзеров через докер -> docker-compose exec web python manage.py startapp accounts
В созданном app в моделях создаётся новая модель, которая будет расширять функционал базы
В settings регистрируется новый app И в самом низу пишется AUTH_USER_MODEL = 'accounts.CustomUser', которая будет заменять дефолтные значения
Makemigrations и migrate в консоли докера.
В accounts создается forms.py в котором будет созданы формы для расширения дефолтных настроек аккаунта и для новых аккаунтов.
в accounts/admin.py добавляется новая модель юзера и формы для представления в админке.
Создаем суперюзера docker-compose exec web python manage.py createsuperuser
Для проверки правильной настройки на данном этапе в accounts/tests выполним проверку. Так как дефолтные настройки были изменены, на данном этапе следует это сделать. docker-compose exec web python manage.py test
Не забываем коммит и пуш в гит периодически.
На данном этапе мы изменили стандартную регистрацию и изменение форм для новых аккаунтов, в моделях создан CustomUser к которому можно добавлять новые поля. Также все отображается в админке

-----------------------------------------------------------------
ЧАСТЬ 3 - СОЗДАНИЕ СТРАНИЦ САЙТА
-----------------------------------------------------------------
