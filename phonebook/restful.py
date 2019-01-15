from bottle import request, response, hook, route
from bottle import post, get, run
from accessdb import find_contact, add_contact


_allow_origin = '*'
_allow_methods = 'GET, POST, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'


# Обработка клиентских запросв к API с других доменов
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = _allow_origin     # принимать запросы с любых URL-адресов
    response.headers['Access-Control-Allow-Methods'] = _allow_methods   # допустимые методы
    response.headers['Access-Control-Allow-Headers'] = _allow_headers   # допустимые заголовки


# Обработка OPTIONS-запросов от клиента к API
@route('/', method='OPTIONS')
@route('/<path:path>', method='OPTIONS')
def options_handler(path=None):
    return


# Обработка GET-запросов, поиск контакта
@get('/contact/<name>')
def getContact(name):
    contact = find_contact(name)
    return contact


# Обработка POST-запросов, добавление контакта
@post('/contact/')
def addContact():
    result = ""
    new_contact = {'name': request.json.get('name'), 'phone': request.json.get('phone')}
    if not new_contact["name"]:                                     # проверка валидности имени
        result = "Имя не указано!"
    elif not new_contact['phone']:                                  # проверка валидности номера
        result = "Телефон указан некорректно! Формат: 89887776655"
    elif type(new_contact['phone']) != int:
        result = "Телефон указан некорректно! Формат: 89887776655"
    elif find_contact(new_contact['name']):                         # проверка существования контакта в БД
        result = "Контакт с таким именем уже существует!"
    else:                                                           # добавление контакта в БД
        add_contact(new_contact['name'], new_contact['phone'])
        result = "Контакт успешно добавлен."
    return {'result': result}


if __name__ == "__main__":
    run(host='127.0.0.1', port=80, reloader=True, debug=False)
