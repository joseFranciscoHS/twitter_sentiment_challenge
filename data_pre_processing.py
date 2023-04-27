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

def data_pre_processing(df):

    try:
        ##Tranlate to english
        trans = []
        ###Loop translate each item in the language_text, translate it and add the translation to the trans list and the detected source language to the language list.
        for  i in df.index:
            translator = Translator()
            translation = translator.translate(df['content'][i], dest = 'en') 
            trans.append(translation.text)  
        ###Add the trans and language list to the data frame and display.
        df['clean_tweet'] = trans

        print("Column 'clean_tweet' added to datafram && content translated to English")

        ##Remove null values
        df = df.dropna()
        null_values = df.isnull().sum()
        print("""Null values removed:
        {}""".format(null_values))

        ##Remove duplicate values
        duplicate_content = len(df['clean_tweet'])-len(df['clean_tweet'].drop_duplicates())
        if duplicate_content > 0:
            df = df.drop_duplicates()
            print("{} duplicate values have been removed".format(duplicate_content))
        else:
            print("There are no duplicate values")

        ## Punctuation removal 
        sep = '|'
        punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~' #string.punctuation
        mapping_table = str.maketrans(dict.fromkeys(punctuation_chars, ''))
        df['clean_tweet'] = pd.Series(sep.join(df['clean_tweet'].tolist()).translate(mapping_table).split(sep))
        print("Punctuation removed from Tweet")

        ##Remove numbers
        df['clean_tweet'] = df['clean_tweet'].str.replace('\d+', '')
        print("Numbers removed from Tweet")

        ##Remove URL's
        regex = r'(\s)http\w+'

        for i in df.index:
            ##Remove emoji
            df['clean_tweet'][i] = emoji.replace_emoji(df['clean_tweet'][i], replace='')

            ##Remove URL's
            if re.findall(regex, df['clean_tweet'][i]):
                df['clean_tweet'][i] = re.sub(regex, '', df['clean_tweet'][i])
            else:
                df['clean_tweet'][i]

            ##Remove Whitespaces
            df['clean_tweet'][i] = ' '.join(df['clean_tweet'][i].split())

            ##Lowering the text
            df['clean_tweet'][i] = df['clean_tweet'][i].lower()

        print("Emoji, URL, whitespaces removed and lower from tweet")

        ##Stop words removal
        stop = stopwords.words('english')
        df['clean_tweet'] = df['clean_tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
        print("Stop words removed from tweet")

        ##Lemmatization
        lemmatizer = WordNetLemmatizer()
        def lemmatize_words(text):
            words = text.split()
            words = [lemmatizer.lemmatize(word,pos='v') for word in words]
            return ' '.join(words)
        df['clean_tweet'] = df['clean_tweet'].apply(lemmatize_words)
        print("Lemmatization has been done")

        return df

    except NameError:
        print("Parameters are not defined")

    except:
        print("Something else went wrong")




