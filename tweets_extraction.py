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
##Tranlate to english
###Create an empty list to contain the translations and the auto detected languages
trans = []
###Loop translate each item in the language_text, translate it and add the translation to the trans list and the detected source language to the language list.
for  i in df.index:
    translator = Translator()
    translation = translator.translate(df['content'][i], dest = 'en') 
    trans.append(translation.text)  
###Add the trans and language list to the data frame and display.
df['clean_tweet'] = trans

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
duplicate_content=len(df['clean_tweet'])-len(df['clean_tweet'].drop_duplicates())
"""0"""
df = df.drop_duplicates()

## Punctuation removal 
sep = '|'
punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~' #string.punctuation
mapping_table = str.maketrans(dict.fromkeys(punctuation_chars, ''))
df['clean_tweet'] = pd.Series(sep.join(df['clean_tweet'].tolist()).translate(mapping_table).split(sep))

##Remove emoji
for i in df.index:
    df['clean_tweet'][i] = emoji.replace_emoji(df['clean_tweet'][i], replace='')

##Remove numbers
df['clean_tweet'] = df['clean_tweet'].str.replace('\d+', '')

##Remove URL's
for i in df.index:
    regex = r'(\s)http\w+'
    if re.findall(regex, df['clean_tweet'][i]):
        df['clean_tweet'][i] = re.sub(regex, '', df['clean_tweet'][i])
    else:
        df['clean_tweet'][i]

##Remove Whitespaces
for i in df.index:
    df['clean_tweet'][i] = ' '.join(df['clean_tweet'][i].split())

##Lowering the text
for i in df.index:
    df['clean_tweet'][i] = df['clean_tweet'][i].lower()

##Stop words removal
import nltk
#>>nltk.download()
from nltk.corpus import stopwords
stop = stopwords.words('english')
df['clean_tweet'] = df['clean_tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

##Lemmatization
##>nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word,pos='v') for word in words]
    return ' '.join(words)
df['clean_tweet'] = df['clean_tweet'].apply(lemmatize_words)

#3.Sentiment Analysis
##Sentiment results
def analize_sentiment(tweet):
    try:
        return TextBlob(tweet).sentiment
    except:
        return None
df['sentiment_results']=df['clean_tweet'].apply(analize_sentiment)

##Add column polarity and subjectivity
polarity = []
subjectivity = []
for  i in df.index:
    list_sr=list(df['sentiment_results'][i]) 
    polarity.append(list_sr[0])  
    subjectivity.append(list_sr[1]) 
df['polarity'] = polarity
df['subjectivity'] = polarity

##Final sentiment
def sentiment(x):
    if x > 0:
        return 'positive'
    elif x == 0:
        return 'neutral'
    else:
        return 'negative'

df['sentiment']=df['polarity'].apply(sentiment)

print(df[['sentiment_results','polarity','subjectivity','sentiment']])

"""
COMENTARY SECTION
for i in df.index:
    print(i, df['translation'][i])

print(df.head())
"""




