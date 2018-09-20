#!/usr/bin/env python
# encoding: utf-8
#Author - Jiarui Jin

import tweepy
from tweepy import OAuthHandler
import json
import wget
from urllib.request import urlretrieve
import subprocess
import argparse
import os

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_key = "access_key"
access_secret = "access_secret"


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
        
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    #.append different?
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print( "...%s tweets downloaded so far" % (len(alltweets)))
       
    picNum = 1
    for status in alltweets:
        entities = status._json.get('entities')
        media = entities.get('media', [{}])
        mediaDic = media[0]
        mediaURL = mediaDic.get('media_url', '')
        mediaName = str(picNum) + ".jpg"
        if mediaURL != '':
           URL = mediaURL
           urlretrieve(URL, mediaName)
           picNum += 1
def mpegvideo():
    ffmpeg_command = 'ffmpeg -framerate 0.25 -i %d.jpg output.mp4'
    subprocess.call(ffmpeg_command, shell=True)

if __name__ == '__main__': 
    #pass in the username of the account you want to download
    get_all_tweets("@Ibra_official")
    mpegvideo()
