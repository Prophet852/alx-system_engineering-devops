#!/usr/bin/python3
"""Function to query number of subcribers on a given reddit subreddit """

  import requests
def number_of_subcribers(subreddit);
"""Return the total number of subcribers on a given subreddit"""
url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {
  "user-Agent": "Linux:0x16.api.advanced:v1.0.0 9by /u/prophet852_)"
}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 404:
    return 0
results = response.json().get("data")
return results.get("subscribers")
