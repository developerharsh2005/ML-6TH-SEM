import tweepy
import csv

api_key = "API_KEY"
api_secret = "API_SECRET"
access_token = "ACCESS"
access_secret = "ACCESS_SECRET"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

query = "Artificial Intelligence"
tweets = api.search_tweets(q=query, lang="en", count=20)

with open("tweets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Tweet"])

    for t in tweets:
        writer.writerow([t.text])

print("tweets.csv created")
