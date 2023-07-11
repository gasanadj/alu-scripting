#!/usr/bin/python3
import requests
"""This module returns the titles of the first 10
hot posts for a subreddit"""


def top_ten(subreddit):
    BASE_URL = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'Didas Junior'}
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        result = response.json()
        data = result.get('data').get('children')
        titleArray = []
        for item in data:
            title = item.get('data').get('title')
            titleArray.append(title)
        for i in range(10):
            print(titleArray[i])
    else:
        print(None)
