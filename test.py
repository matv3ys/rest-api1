from requests import get, delete, put

# запрос всех работ до редактирования
print(get('http://localhost:5000/api/jobs').json())

# корректный запрос на редактирование
print(put('http://localhost:5000/api/jobs/6', json={'id': 7,
                                                    'job': 'Теcтировать редактирование',
                                                    'team_leader': 5,
                                                    'work_size': 1,
                                                    'collaborators': '2, 3',
                                                    'is_finished': False}).json())

# запрос всех работ после редактирования
print(get('http://localhost:5000/api/jobs').json())

# пустой запрос
print(put('http://localhost:5000/api/jobs/3').json())

# некорректный запрос (несуществующий id)
print(put('http://localhost:5000/api/jobs/100', json={'job': 'наш'}).json())

# некорректный запрос (ключ title не существует)
print(put('http://localhost:5000/api/jobs/3', json={'title': 'марс'}).json())
