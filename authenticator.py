import tweepy
import os

def authenticate():

    # THE ENVIRONMENT VARIABLES TO NOT EXPOSE YOUR KEYS (API KEY & API SECRET FROM TWITTER)
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    # THE ENVIRONMENT VARIABLES TO NOT EXPOSE YOUR KEYS (ACCESS TOKEN & TOKEN SECRET FROM TWITTER)
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("TOKEN_SECRET")

    # THE TWEEPY LIB DOES THE MAGIC HERE
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # WE CAN CALL IT WHENEVER WE WANT TO AUTHENTICATE THE ACCESS (TO TWEET, FOR EXAMPLE)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if __name__ == "__main__":
    authenticate()