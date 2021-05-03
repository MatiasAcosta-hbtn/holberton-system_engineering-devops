#!/usr/bin/python3
"""Using an API with python"""

import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        url = 'https://jsonplaceholder.typicode.com/users'
        r = requests.get('{}/{}/todos'.format(url, argv[1]))
        user = requests.get('{}/{}'.format(url, argv[1]))
        user = user.json().get('name')
        todo = r.json()
        text = ""
        completed = 0
        for task in todo:
            if task.get('completed') is True:
                completed += 1
                text += "\t {}\n".format(task.get('title'))
        print("Employee {} is done with tasks({}/{}):"
              .format(user, completed, len(todo)))
        print(text, end="")
