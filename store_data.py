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
#import pymysql
#from sqlalchemy import create_engine
from datetime import datetime
import pyodbc


loc = "23.634501, -102.552784, 1789km"
query = '(Biden OR biden) until:2023-03-20 since:2023-03-03 geocode:"{}"'.format(loc) 
tweets = []
limit = 50000
df_1 = data_collection.data_collection(query, limit)
df_2 = data_pre_processing.data_pre_processing(df_1)
data = sentiment_analysis.sentiment_analysis(df_2)

#Change dataframe to csv
#filename_list = []
filename = datetime.timestamp(datetime.now())
#filename_list.append(filename)

data.to_csv(r'C:\Users\CASA\Portafolio\digital_NAO\twitter_sentiment_challenge\csv\{}.csv'.format(filename),encoding = 'utf-8', index=False)
print("CSV file has been saved")



#c_write_to_file('oneliner_cython.csv', df_to_string(df,str_format).encode("UTF-8"))
#%timeit -r3 df.to_csv('tocsv.csv',index=False,float_format='%10.11f')

"""
chain_connection = 'mysql+pymysql://root:Elhe1005lore27**@localhost:3306/twitterdb'
connection = create_engine(chain_connection)
data.to_sql(name='tweets', con = connection)
"""

