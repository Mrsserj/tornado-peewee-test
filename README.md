Tornado PeeWee Test

 Пример ассинхронного приложения с использованием tornado и ORM Peewee
 
 Для запуска приложения:
 
 * установите необходимые модули `pip install -r requirements.txt`
 * отредактируйте файл settings.py согласно настройкам вашего сервера СУБД Postgres
 * запустите сервер командой `>python server.py`
 * запуск теста `python.exe -m tornado.test.runtests tests.TestListTest.TestCase`
 
Интерфейс приложения по умолчанию доступен по адресу http://127.0.0.1:5000

Тестировалось с python 3.8
При инициализации базы создается суперпользователь "test" с паролем "test12345"
Так же создаются тестовые вопросы.