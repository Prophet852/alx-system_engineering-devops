#!/usr/bin/python3
"""Function to query number of subcribers on a given reddit subreddit """

<<<<<<< HEAD
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
    


=======
  import requests
def number_of_subcribers(subreddit);
"""Return the total number of subcribers on a given subreddit"""
url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {
  "user-Agent": "Linux:0x16.api.advanced:v1.0.0 9by /u/bdov_)"
}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 404:
    return 0
results = response.json().get("data")
return results.get("subscribers")
>>>>>>> 36d47b3fc0615ff0c44a960456b2a3b06c417e2c
