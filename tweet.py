'''
tweet.py: tweet bot to tweet code quetions
21 January 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
import time

from os import environ

from get_question import get_question
from get_reply import get_reply

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    interval = 60 * 60 * 6  # seconds * minutes * hours
    reply_with = get_reply()
    # reply_with = 'Here\'s our question! \nStick around, we\'ll have another in 6 hours! \n\n🤷It may be easy, it may be hard. \n⌨️Either way, give it a tweet \n🔎Don\'t know it? Look it up \n❓Still unsure? Ask'

    while True:
        print("finding a question...")
        question = get_question()
        print("chose question: " + question)
        tweet = api.update_status(question)  # variable used later for reply to this tweet
        print('question has been tweeted')
        api.update_status(status=reply_with, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
        print('chose reply:' + reply_with)
        print('reply has been tweeted')
        time.sleep(interval)


main()
