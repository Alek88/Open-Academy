
url = 'http://localhost:8569'
db = 'o15-learn'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

sessions_all = models.execute_kw(db, uid, password, 'openacademy.sessions', 'search_read', [[]], {'fields': ['name', 'occupied_of_seats'],'limit': 0})
for session in sessions_all:
    print(session)

print()

create_new_item = ''
tiontions = ''
while create_new_item != 'y' or create_new_item != 'n':
    create_new_item = input(tiontions + 'Создать новую сессию? Введите "Y" или "N" и нажмите Enter.\n')
    create_new_item = create_new_item.lower()
    if create_new_item == 'y' or create_new_item == 'n':
        break
    else:
        atten = "Не верный ввод! "

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
        courses = models.execute_kw(db, uid, password, 'openacademy.course', 'search_read', [[]], {'fields': ['name'],'limit': 0})
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
        ###

        new_session_id = models.execute_kw(db, uid, password, 'openacademy.sessions', 'create',
                            [{'name': new_session_name, 'number_of_seats': new_session_number_of_seats, 'course': course_id}])

        new_sessions_read = models.execute_kw(db, uid, password, 'openacademy.sessions', 'read', [new_session_id],
                                          {'fields': ['name', 'number_of_seats', 'course']})
        print('Создана новая сессия:')
        print(new_sessions_read)
else:
    print("Сессия не создана.")