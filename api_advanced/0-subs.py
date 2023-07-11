#!/usr/bin/python3
""" This module returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    BASE_URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Didas Junior'}
    response = requests.get(
        BASE_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
