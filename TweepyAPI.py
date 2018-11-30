#!/usr/bin/env python
# encoding: utf-8
#Author - Jiarui Jin

import tweepy
from tweepy import OAuthHandler
import json
import wget
from urllib.request import urlretrieve
import subprocess
import os

consumer_key = 'Enter the consumer_key'
consumer_secret = 'Enter the consumer_secret'
access_token = 'Enter the access_key'
access_secret = 'Enter the access_secret'


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
    while (True):
                #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)

        if (len(new_tweets) == 0):
             break
        else:
        #save most recent tweets
           alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
           oldest = alltweets[-1].id - 1
            
        if(len(alltweets) > 15):
            break
        print( "...%s tweets downloaded so far" % (len(alltweets)))
       

    directory = os.getcwd() + "/" + screen_name
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("already exsist")
    except OSError:
        print(('Error: Creating directory. ' + directory))

    picNum = 1
    for status in alltweets:
        entities = status._json.get('entities')
        media = entities.get('media', [{}])
        mediaDic = media[0]
        mediaURL = mediaDic.get('media_url', '')
        mediaName = directory + "/" + str(picNum) + ".jpg"

        if mediaURL != '':
            URL = mediaURL
            urlretrieve(URL, mediaName)
            picNum += 1
            if (picNum == 11):
                print('already download 10 pictures')
                break


def mpegvideo(screen_name):
    ffmpeg_command = 'ffmpeg -r 1  -i D:/EC601/mini_project3/@KicksFinder/%d.jpg  -y output.mp4'
    subprocess.call(ffmpeg_command, shell=True)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@KicksFinder")
    mpegvideo("@KicksFinder")
