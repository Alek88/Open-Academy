import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8569
DB = 'o15-learn'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

#Отобразить все сессии
sessions_oll = call(url, "object", "execute", DB, uid, PASS, "openacademy.sessions", 'search_read', [], ['name', 'occupied_of_seats'])
for session in sessions_oll:
    print(session)

#Создать новую сессию для выбранного курса
create_new_item = ''
attentions = ''
while create_new_item != 'y' or create_new_item != 'n':
    create_new_item = input(attentions + 'Создать новую сессию? Введите "Y" или "N" и нажмите Enter.\n')
    create_new_item = create_new_item.lower()
    if create_new_item == 'y' or create_new_item == 'n': break
    else: attentions = "Не верный ввод! "

new_session_name = ''
new_session_number_of_seats = 0
if create_new_item == 'y':
    while new_session_name == '':
        new_session_name = input('Введите имя сессии.\n')
        if new_session_name == '':
            print('Имя не может быть пустым.')
            continue

        new_session_number_of_seats = input('Введите количество мест.\n')

        if new_session_number_of_seats == '':
            new_session_number_of_seats = 0
        else:
            new_session_number_of_seats = int(new_session_number_of_seats)

        courses_list_id = []
        print('Доступные курсы:')
        courses = call(url, "object", "execute", DB, uid, PASS, "openacademy.course", 'search_read', [],
                       ['name', 'date_learning'])
        for course in courses:
            courses_list_id.append(course['id'])
            print(course)

        in_course_id = False
        course_id = 0
        while not in_course_id:
            course_id = int(input('Укажите идентификатор курса для которой будет создана сессия.\n'))
            if course_id in courses_list_id:
                in_course_id = True
            else:
                print('Курс с указанным идентификатором не найден, повротите попытку.')

        args = [
            {'name': new_session_name,
             'course': course_id,
             'occupied_of_seats': new_session_number_of_seats
             }
        ]
        new_session_id = call(url, 'object', 'execute', DB, uid, PASS, 'openacademy.sessions', 'create', args)
        print(f'Создана новая сессия: {new_session_name}')
else:
    print("Сессия не создана.")


