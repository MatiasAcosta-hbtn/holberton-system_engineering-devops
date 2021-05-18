#!/usr/bin/python3
"""Working with Reddit API"""


import requests


def number_of_subscribers(subreddit):
    """function that returns the total number of
    subscribers for a given subreddit"""
    headers = {'User-Agent': 'Holberton/2.0.21'}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=headers)
    if res.status_code == 200:
        return (res.json().get('data').get('subscribers'))
    else:
        return 0
