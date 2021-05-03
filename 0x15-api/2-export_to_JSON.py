#!/usr/bin/python3
"""Using an API with python"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        url = 'https://jsonplaceholder.typicode.com/users'
        r = requests.get('{}/{}/todos'.format(url, argv[1]))
        r2 = requests.get('{}/{}'.format(url, argv[1]))
        username = r2.json().get('username')
        user = r2.json().get('id')
        todo = r.json()
        data = {}
        new_list = []
        for task in todo:
            new_list.append({"task": task.get('title'),
                             "completed": task.get('completed'),
                             "username": username})
        data[user] = new_list
        with open('{}.json'.format(user), 'w') as file:
            json.dump(data, file)
