#!/usr/bin/python3
"""
Function to query number of subcribers on a given reddit subreddit """

import requests

def number_of_subcribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = request.get(url, heads=headers, allow_redirects=false)
    
    If response .status_code !=200:
        return 0
        
    data = response.json().get("data)
    num_subs = data.get("subcribers")
    
    return num_subs
    


