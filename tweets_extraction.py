import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob
import string
import re
import emoji
from googletrans import Translator

#1. Data collection
loc = "23.634501, -102.552784, 1789km"
query = '(mexico OR méxico OR Mexico OR México) until:2023-02-28 since:2023-02-01 geocode:"{}"'.format(loc) 
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
     
    if len(tweets) == limit:
        break
    else: 
        tweets.append([tweet.id, tweet.date, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang])

df = pd.DataFrame(tweets, columns = ['id', 'date', 'content','reply_count', 'retweet_count', 'like_count', 'language'])

#2. Data pre-processing
## Punctuation removal 
sep = '|'
punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~' #string.punctuation
mapping_table = str.maketrans(dict.fromkeys(punctuation_chars, ''))
df['content'] = pd.Series(sep.join(df['content'].tolist()).translate(mapping_table).split(sep))

##Remove numbers
df['content'] = df['content'].str.replace('\d+', '')

##Remove duplicates
null_values = df.isnull().sum()
"""
id               0
date             0
content          0
reply_count      0
retweet_count    0
like_count       0
language         0
"""
duplicate_rows = len(df)-len(df.drop_duplicates()) 
"""0"""
duplicate_content=len(df['content'])-len(df['content'].drop_duplicates())
"""0"""
##Remove URL's
for i in df.index:
    regex = r'(\s)http\w+'
    if re.findall(regex, df['content'][i]):
        df['content'][i] = re.sub(regex, '', df['content'][i])
    else:
        df['content'][i]

##Remove Whitespaces
for i in df.index:
    df['content'][i] = ' '.join(df['content'][i].split())

##Lowering the text
for i in df.index:
    df['content'][i] = df['content'][i].lower()

##Remove emoji
for i in df.index:
    df['content'][i] = emoji.replace_emoji(df['content'][i], replace='')

##Tranlate to english
###Create an empty list to contain the translations and the auto detected languages
trans = []
###Loop translate each item in the language_text, translate it and add the translation to the trans list and the detected source language to the language list.
for  i in df.index:
    translator = Translator()
    translation = translator.translate(df['content'][i], dest = 'en') 
    trans.append(translation.text)  
###Add the trans and language list to the data frame and display.
df['translation'] = trans

##Stop words removal
import nltk
#>>nltk.download()
from nltk.corpus import stopwords
stop = stopwords.words('english')
# Exclude stopwords with Python's list comprehension and pandas.DataFrame.apply.
df['tweet_without_stopwords'] = df['translation'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
#print(df[['translation', 'tweet_without_stopwords']])
for i in df.index:
    print(i, df['tweet_without_stopwords'][i])

"""
COMENTARY SECTION

for i in df.index:
    print(i, df['content'][i])
"""



