#!/usr/bin/python3
"""Working with Reddit API"""
import requests


def top_ten(subreddit):
    """Function that prints the top ten
    hottest posts for a given subreddit."""
    headers = {'User-Agent': 'Holberton/2.0.21'}
    response = requests.get(
                            'https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit), headers=headers,
                            allow_redirects=False)
    values = response.json()
    if response.status_code == 200:
        for i in range(10):
            print(values['data']['children'][i]['data']['title'])
    else:
        print("None")
