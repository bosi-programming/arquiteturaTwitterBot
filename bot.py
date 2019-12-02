import tweepy
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

searches = api.search(q='arquitetura', count=10, result_type='recent')

best_tweet = 0

for i in range(len(searches)):
    if searches[i].retweet_count > searches[best_tweet].retweet_count:
        best_tweet = i

id = searches[best_tweet].id

api.retweet(id)