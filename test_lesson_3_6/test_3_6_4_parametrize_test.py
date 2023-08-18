import json

with open('../my_login.json', 'r', encoding='utf-8') as file:
    my_login = json.load(file)
    # print(my_login['login'], my_login['pass'])
