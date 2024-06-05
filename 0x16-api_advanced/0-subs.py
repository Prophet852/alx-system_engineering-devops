#!/usr/bin/python3
"""
Function to query number of subcribers on a given reddit subreddit """

import requests

def get_subreddit_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        subscribers = response['data']['subscribers']
        return subscribers
    except:
        return 0

