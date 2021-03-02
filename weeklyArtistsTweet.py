import urllib.request
import json
import authenticator
import os
import time

# GET THE CURRENT TIME AND THE TIME FROM THE LAST WEEK IN THE UNIX TIMESTAMP
current_time = int(time.time())
last_week = current_time - 604800

# THE ENVIRONMENT VARIABLES TO NOT EXPOSE YOUR KEYS
last_key = os.getenv("LAST_KEY")
last_username = os.getenv("LAST_USERNAME")

# CONVERT THE JSON FROM THE LASTFM API TO A DICTIONARY SO WE CAN READ IT IN THE CODE
json_file = urllib.request.urlopen(f"http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user={last_username}&api_key={last_key}&from={last_week}&to={current_time}&format=json").read()
obj = json.loads(json_file.decode())

# THIS PART DETERMINATES HOW MANY ARTISTS WE LISTENED DURING THE WEEK
range_number = (len(obj['weeklyartistchart']['artist'])) 

# INITIALIZE A LIST SO WE CAN WRITE A BETTER TWEET
the_list = []

# WE WANT JUST THE TOP10 ARTISTS OF THE WEEK, THIS IF WILL HELP US WITH THAT
if range_number > 10:
    range_number = 10

# CREATE AN INDEX TO SEARCH THE JSON OBJECT THAT WE CREATED
for index in range(range_number):
    
    # GET THE ARTISTS THAT WE LISTENED DURING THE WEEK
    artist = (obj['weeklyartistchart']['artist'][index]['name'])
    # GET HOW MANY TIMES WE LISTENED TO THAT ARTIST
    scroobles = (obj['weeklyartistchart']['artist'][index]['playcount'])

    # ADD THE ARTISTS/SCROOBLES IN THE LIST THAT WE CREATED BEFORE
    x = artist + " (" + scroobles + ")"
    the_list.append(x)

tweet_head = "Os mais ouvidos da semana:\n"
tweet_end = "#VitinhosFM"
# SEPARATES THE LIST WITH THE COMMA. THIS IS THE FINAL TEXT, WE CAN TWEET IT!
the_tweet = tweet_head + ', '.join(the_list) + " " + tweet_end

# CALLS THE AUTHENTICATION
api = authenticator.authenticate()

# THE MAIN USES THE TWEEPY UPDATE_STATUS TO POST THE TWEET
if __name__ == "__main__":
    api.update_status(the_tweet)