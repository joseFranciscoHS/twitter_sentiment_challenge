#DATA COLLECTION==================================================
import snscrape.modules.twitter as sntwitter
import pandas as pd
#DATA PRE-PROCESSING===============================================
import data_collection
import string
import re
import emoji
from googletrans import Translator
import nltk
#>>nltk.download()
from nltk.corpus import stopwords
##>nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
#SENTIMENT ANALYSIS====================================================
import data_pre_processing
from textblob import TextBlob

def sentiment_analysis(df):

    try:
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

        return df

    except NameError:
        print("Parameters are not defined")

    except:
        print("Something else went wrong")



