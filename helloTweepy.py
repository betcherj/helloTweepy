import tweepy
import time
import os
import configparser
import random

config_file = dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\tweepy_config.ini"

config = configparser.ConfigParser()
config.read(config_file)
tokens = config._sections['tokens']
#authentication
auth = tweepy.OAuthHandler(tokens['pk'], tokens['sk']
)

auth.set_access_token(tokens['acesstoken'], tokens['acesstokensecret']
)
api = tweepy.API(auth, wait_on_rate_limit = True)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

user = api.get_user('jackybetch')

friends = api.friends_ids('jackybetch')
for friend in friends:
    temp = api.friends_ids(friend)
    time.sleep(random.randint(0,10))
    if len(temp)<400:
        if user.id not in temp:
            print(api.get_user(friend).screen_name, 'doesnt follow back')

public_tweets = api.home_timeline()

