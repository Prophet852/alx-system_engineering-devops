#!/usr/bin/python3
"""
<<<<<<< HEAD
Function to query number of subcribers on a given reddit subreddit """
=======
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
>>>>>>> 3dc0ef0de0372eecc0603b71f2cd903ec93c4c43

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
<<<<<<< HEAD
    headers = {
            "User-Agent":"linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subcribers")
=======
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
>>>>>>> 3dc0ef0de0372eecc0603b71f2cd903ec93c4c43
