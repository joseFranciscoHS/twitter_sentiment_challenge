#DATA COLLECTION======================================================
import snscrape.modules.twitter as sntwitter
import pandas as pd

def data_collection(query, limit):

    try:
        tweets = []

        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            
            if len(tweets) == limit:
                break
            else: 
                tweets.append([tweet.id, tweet.date, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.lang])

        df = pd.DataFrame(tweets, columns = ['id', 'date', 'content','reply_count', 'retweet_count', 'like_count', 'language'])

        print("The data collection was successful")
        return df
        

    except NameError:
        print("Parameters are not defined")

    except:
        print("Something else went wrong")

        

