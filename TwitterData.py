#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tweepy, json
import pandas as pd


# In[3]:


# auth = tweepy.OAuthHandler('uBdYOH9ZNIZ3nzjOffdOoPzk4', 'UKDo1Z9Aa9IYUrxAnFEAqruNlzJnKJ6FEaPAwDnbx8h4EDuwOw')
# auth.set_access_token('1463605105840820225-Wmnk5ZqMOvygaPW2IiuMRbtOY0nFfA', 'HwlczAGv8yy7eVAYcMxcgaasZDEGelL7IA59nsYYML241')
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAB6ZWAEAAAAAfJvmx9F6G0MDnmhLDJArok%2Be8DQ%3DVUcIjorrsQQa2PLuwLgs7q81znlHId0DqfwxmlCuEHNflfjZFe')
query = 'COVID, MASKS, VACCINE'
#tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], place_fields=['country_code', 'geo'], expansions='geo.place_id', max_results=100)


# In[4]:


tweets = []
for response in tweepy.Paginator(client.search_recent_tweets, 
                                 query = 'COVID, MASKS, VACCINE',
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 place_fields = ['country_code'],
                                 expansions = 'author_id',
                                 #start_time = '2021-12-11T00:00:00Z',
                                 #end_time = '2021-12-16T00:00:00Z',
                              max_results=100):
    tweets.append(response)


# In[5]:


tweets[0].includes['users'][3]


# In[6]:


tweets[0].includes['users'][3]


# In[7]:


result = []
user_dict = {}
# Loop through each response object
for response in tweets:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
    for user in response.includes['users']:
        user_dict[user.id] = {'username': user.username, 
                              'followers': user.public_metrics['followers_count'],
                              'tweets': user.public_metrics['tweet_count'],
                              'description': user.description,
                              'location': user.location
                             }
    for tweet in response.data:
        # For each tweet, find the author's information
        author_info = user_dict[tweet.author_id]
        # Put all of the information we want to keep in a single dictionary for each tweet
        result.append({'author_id': tweet.author_id, 
                       'username': author_info['username'],
                       'author_description': author_info['description'],
                       'author_location': author_info['location'],
                       'text': tweet.text,
                       'created_at': tweet.created_at,
                       'retweets': tweet.public_metrics['retweet_count'],
                       'replies': tweet.public_metrics['reply_count'],
                       'quote_count': tweet.public_metrics['quote_count']
                      })

# Change this list of dictionaries into a dataframe
df = pd.DataFrame(result)


# In[8]:


result


# In[9]:


df


# In[ ]:





# In[ ]:





# In[ ]:




