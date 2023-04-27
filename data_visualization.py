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
#STORE DATA================================================================
import sentiment_analysis
import pymysql
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from PIL.Image import core as _imaging
import numpy as np
#import seaborn as sns

import warnings
warnings.filterwarnings(action = 'ignore')

loc = "23.634501, -102.552784, 1789km"
query = '(mexico OR méxico OR Mexico OR México) until:2023-02-28 since:2023-02-01 geocode:"{}"'.format(loc) 
tweets = []
limit = 100
df_1 = data_collection.data_collection(query, limit)
df_2 = data_pre_processing.data_pre_processing(df_1)
data = sentiment_analysis.sentiment_analysis(df_2)

#data = pd.read_csv('../input/banking-churn-prediction/Banking_churn_prediction.csv')

#first 5 instances using "head()" function
print(data.head())

#last 5 instances using "tail()" function
print(data.tail())

#finding out the shape of the data using "shape" variable: Output (rows, columns)
print(data.shape)

#Printing all the columns present in data
print(data.columns)

# A closer look at the data types present in the data
print(data.dtypes)



#Question 1: ¿Cuáles son las palabras más empleadas?, WORDCLOUD TOPIC
#Question 2: ¿Qué sentimiento es más intenso?, EMBUDO
#Question 3: ¿Qué tan objetivos son los Tweets sobre el tema?, 
#Question 4:¿Qué tan positivos se espera que sean los comentarios para el día de mañana?”.

