import tweepy
#authentication
auth = tweepy.OAuthHandler('TsNTi5WMTYQzXhwFOGdJC3X8L', 'wn6EKOTVzBMIpMRYhfOIVKKc3qbcYiTRBUhsDlBjjd9AwkGqft'
)
auth.set_access_token('586132573-WRDsgPNNAofrIhMZYZ9p2gm2EIGTQ47uWampLh4M', 'mK3uxoYCBvqzlHW35JdEevhfyig55KnICGhDTnNK53yNl'
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
    if len(temp)<400:
        if user.id not in temp:
            print api.get_user(friend).screen_name, 'is a little bitch'

public_tweets = api.home_timeline()

