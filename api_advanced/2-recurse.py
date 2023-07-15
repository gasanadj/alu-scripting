#!/usr/bin/python3
""" This module uses recursion to get hot articles"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    
    BASE_URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Didas Junior'}
    params = {'after': after}
    response = requests.get(BASE_URL, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    recurse(subreddit, hot_list, after)

        return 'OK'
    else:
        return None


