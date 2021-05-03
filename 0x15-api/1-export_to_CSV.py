#!/usr/bin/python3
"""Using an API with python"""

import csv
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
    with open('{}.csv'.format(user), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user, username,
                            task.get('completed'), task.get('title')])
