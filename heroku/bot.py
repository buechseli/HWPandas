
# coding: utf-8

# In[7]:


# Dependencies
import numpy as np
import tweepy
from pprint import pprint
import time
import json
import random
import requests 
import datetime
from config import API_Key , API_Secret, Token, Token_Secret




# In[8]:


# Twitter API Keys
consumer_key = API_Key
consumer_secret = API_Secret
access_token = Token
access_token_secret = Token_Secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[9]:


# Target Term
target_term = "@Isa_EscRiv"


# In[10]:


# Opening message
print("We're going live!")


# In[19]:


# Create Thank You Function
def ThankYou():


    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets

    for tweet in public_tweets["statuses"]:
        tweet_author=tweet["user"]["screen_name"]
        
        try:
            api.update_status("Hey @"+tweet_author+"! YOU ARE COOL!")
        except Exception:
            print("I ALREADY DID THAT")

   
        # Get ID and Author of most recent tweet directed to me

        # Print the tweet_id


        # Use Try-Except to avoid the duplicate error


            # Print success message


            # Print message if duplicate


        # Print message to signify complete cycle
        


# In[ ]:


while(True):
    ThankYou()
    time.sleep(60)

