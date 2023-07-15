#!/us/bin/python3
"This return hot list"
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Headers for the Reddit API
    headers = {'User-Agent': 'Didas Junior'}

    # Request URL with pagination if applicable
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return None

    # Load the JSON data from the response
    data = response.json()

    # Get the list of posts
    posts = data['data']['children']

    # Add the titles of the posts to the hot_list
    for post in posts:
        hot_list.append(post['data']['title'])

    # Check if there are more posts
    after = data['data']['after']
    if after:
        # Call the function again with the new 'after' value
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
