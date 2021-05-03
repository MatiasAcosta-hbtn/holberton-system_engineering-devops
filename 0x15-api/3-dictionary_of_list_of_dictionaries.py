#!/usr/bin/python3
"""Using an API with python"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    all_users = requests.get('{}'.format(url))
    all_users = all_users.json()
    total_data = {}
    for user in all_users:
        r = requests.get("{}/{}/todos".format(url, user.get('id')))
        username = user.get('username')
        user_id = user.get('id')
        todo = r.json()
        data = {}
        new_list = []
        for task in todo:
            new_list.append({"task": task.get('title'),
                             "completed": task.get('completed'),
                             "username": username})
        total_data[user_id] = new_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(total_data, file)