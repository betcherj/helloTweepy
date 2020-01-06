
from tweepy import *
import configparser
import os
import time
import random

class MyListiner(StreamListener):

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
        for hashtag in status.entities['hashtags']:
            print(hashtag['text'])

        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        if status_code == '402':
            time.sleep(random.randint(10,50))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_file = dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\tweepy_config.ini"
    config.read(config_file)
    tokens = config._sections['tokens']
    listener = MyListiner()
    auth = OAuthHandler(tokens['pk'], tokens['sk'])
    auth.set_access_token(tokens['at'], tokens['ats'])

    stream = Stream(auth, listener)
    stream.filter(follow=['38744894'], track=['#trump'])