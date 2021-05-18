#!/usr/bin/python3
"""Working with Reddit API"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function that recursively returns a list of titles
    for all hot articles on a given subreddit"""
