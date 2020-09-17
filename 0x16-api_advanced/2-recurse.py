#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'API Project by andreshugueth'}
    arguments = {"limit": 100, "after": after}
    r = requests.get(url, params=arguments, headers=headers).json()
    children = r.get("data", {}).get("children", None)
    pagination = r.get("data", {}).get("after", None)

    if pagination is not None:
        if children:
            for topic in children:
                hot_list.append(topic.get("data").get("title"))
        if pagination is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
