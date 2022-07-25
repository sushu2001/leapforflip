import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
 
 #for showiing time

# print(public_tweets[0].user.created_at)

#text
# print(public_tweets[0].user.text)

#who tweeted
# print(public_tweets[0].user.screen_name)

# for tweet in public_tweets:
#     print(tweet.text)

# create dataframe
columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

#print(df)

#data saved to csv file below
df.to_csv('tweets.csv')

#user tweets

user = 'veritasium'
limit = 300
tweets = tweepy.Cursor(api.user_timeline, 
        screen_name=user, count=200, tweet_mode='extended').items(limit)
#the above code is used to solve the problem of not truncating total no. of tweets
#tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode = 'extended')
#"extended" will aloow more than 140 characters and will not truncate the tweets

# for tweet in tweets:
#     print(tweet.full_text)

#search tweets
keywords = '2022'
# for hastags use below code\

# keywords = '#2022'

# for specific user use below

#keywords = '@veritasium'
limit = 300
tweets = tweepy.Cursor(api.search_tweets, q=keywords,
        count=200, tweet_mode='extended').items(limit)

# Stream Real time tweets

# class Listener(tweepy.Stream):
#     def on_status(self, )
