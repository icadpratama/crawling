import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:
        consumer_key = "XbXemJbK6OGKInlId4CQ4FemC"
        consumer_secret = "1RaUNYMLwX0wot3XMTTf1Zt4GQerhhvKhjIdvhrRYhcaDnpOlV"
        access_token = "806750562783854594-neelJGTXDpnA03eI5iNraCLOJzwLS0g"
        access_secret = "2XcI49UsFg87Le4JDjSjCXPaBuY0BkvupESEVe93Gy3ht"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client