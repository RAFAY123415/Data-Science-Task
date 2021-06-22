import tweepy
from tweepy import Stream
from tweepy import StreamListener
import json
from textblob import TextBlob
import re
import csv

bitcoin = 0
ethereum = 0

header_name = ['bitcoin', 'ethereum']
with open('sentiment.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header_name)
    writer.writeheader()

consumerKey ="v4H4K8uUzS0FZGSdWaFArQ"
consumerSecerte="OBTyKbD1c6zuohzInU63YieZMeGtq7JK0HeWfce6k"

consumerToken ="78048591-Ey17sNfTZ3W6Xjv4Ua8TzAooYYBT0SyUXuZfbuVjQ"
consumerTokenSecert="RQ1xyhYWvlOcjZQN6CeA5g8c2CAU0STbc6CsXnu23LsFd"


authenticate = tweepy.OAuthHandler(consumerKey,consumerSecerte)
authenticate.set_access_token(consumerToken, consumerTokenSecert)
#api = tweepy.API(authenticate, wait_on_rate_limit=True)

class Listner (tweepy.StreamListener) :
    def on_data(self, data):
        raw_twitts=json.loads(data)
        tweets = raw_twitts['text']
        tweets = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweets).split())
        tweets = ' '.join(re.sub('RT', ' ', tweets).split())
        blob = TextBlob(tweets.strip())
        #print(blob)
        global bitcoin
        global ethereum

        bitcoin_sentiment=0
        ethereum_sentiment=0
        for sent in blob.sentences:
            if "bitcoin" in sent and "ethereum" not in sent:
                bitcoin_sentiment = bitcoin_sentiment + sent.sentiment.polarity
            else:
                ethereum_sentiment = ethereum_sentiment + sent.sentiment.polarity

        bitcoin = bitcoin + bitcoin_sentiment
        ethereum= ethereum + ethereum_sentiment

        with open('sentiment.csv', 'a') as file:
            writer = csv.DictWriter(file, fieldnames=header_name)
            info = {
                'bitcoin': bitcoin,
                'ethereum': ethereum
            }
            writer.writerow(info)


    def on_error(self, status_code) :
        print(status_code)

twitter_stream=Stream(authenticate,Listner())
twitter_stream.filter(track=['bitcoin','ethereum'])



