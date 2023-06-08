#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
Returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
The function returns None.
"""
import requests


def recurse(subreddit, d_list=[], params={}):
    """
    Returns a list of titles of all hot posts of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    header = {"User-Agent": "MyUser"}

    response = requests.get(url, allow_redirects=False,
                            headers=header, params=params)
    data = response.json().get("data")

    if response.status_code == 404:
        return (None)

    after = data.get("after")
    before = data.get("before")

    if response.status_code == 200:
        ans = data.get("children")
        for item in ans:
            d_list.append(item.get("data").get("title"))

    if after is None:
        return (d_list)

    return recurse(subreddit, d_list,
                   params={"after": after, "before": before})
