#!/usr/bin/python3
"""Working with Reddit API"""
import requests


def count_words(subreddit, word_list):
    """Function that recursively prints a sorted count
    of given keywords parsed from titles of all hot articles
    on a given subreddit"""
