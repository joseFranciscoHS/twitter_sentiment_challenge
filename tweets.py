import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob

query = "(mexico OR méxico OR Mexico OR México) until:2023-02-28 since:2023-02-01"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    #print(vars(tweet))
    #print(len(vars(tweet).keys())) #29
    """
    dict_keys(['url', 'date', 'rawContent', 'renderedContent', 'id', 'user', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount',
    'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel', 'links', 'media', 'retweetedTweet', 'quotedTweet', 
    'inReplyToTweetId', 'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags', 'card', 'viewCount', 'vibe'])   
    """
    #print(vars(tweet).values())
    #print(vars(tweet).items())
    """
    dict_items([('url', 'https://twitter.com/drmwdusa/status/1630357108540448768'), 
    ('date', datetime.datetime(2023, 2, 27, 23, 59, 59, tzinfo=datetime.timezone.utc)), 
    ('rawContent', 'me convidaria para um date no méxico \n\nVAMO MOR'), 
    ('renderedContent', 'me convidaria para um date no méxico \n\nVAMO MOR'), 
    ('id', 1630357108540448768), 
    ('user', User(username='drmwdusa', id=1465322081403428865, displayname='yas | cr: as vantagens de ser invisível', rawDescription='• nobody in this room is alone ❤️\u200d🩹', renderedDescription='• nobody in this room is alone ❤️\u200d🩹', descriptionLinks=None, verified=False, created=datetime.datetime(2021, 11, 29, 14, 12, 20, tzinfo=datetime.timezone.utc), followersCount=5279, friendsCount=5034, statusesCount=9110, favouritesCount=2020, listedCount=12, mediaCount=157, location='be lilith, never eve', protected=False, link=TextLink(text='skoob.com.br/share/user/yas…', url='https://www.skoob.com.br/share/user/yasribeiro', tcourl='https://t.co/LPTWkRdugC', indices=(0, 23)), profileImageUrl='https://pbs.twimg.com/profile_images/1465322869689303040/F3O0bIQb_normal.jpg', profileBannerUrl='https://pbs.twimg.com/profile_banners/1465322081403428865/1670901522', label=None)), 
    ('replyCount', 0), 
    ('retweetCount', 0), 
    ('likeCount', 0), 
    ('quoteCount', 0), 
    ('conversationId', 1630357108540448768), 
    ('lang', 'es'), 
    ('source', '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>'), 
    ('sourceUrl', 'http://twitter.com/download/iphone'), 
    ('sourceLabel', 'Twitter for iPhone'), 
    ('links', None), 
    ('media', None), 
    ('retweetedTweet', None), 
    ('quotedTweet', Tweet(url='https://twitter.com/LouisAccessBR/status/1630305816359084034', date=datetime.datetime(2023, 2, 27, 20, 36, 10, tzinfo=datetime.timezone.utc), rawContent='O QUE O LOUIS FARIA POR VOCÊ? 🤔\n  \nMe contem aqui nos comentários! https://t.co/a6ZlgpPoZG', renderedContent='O QUE O LOUIS FARIA POR VOCÊ? 🤔\n  \nMe contem aqui nos comentários! https://t.co/a6ZlgpPoZG', id=1630305816359084034, user=User(username='LouisAccessBR', id=1458233634708672518, displayname='Louis Access Brasil', rawDescription='Sua fonte de notícias sobre o cantor e compositor Louis Tomlinson no Brasil! | Fan Account \nhttps://t.co/qDuFir8dib', renderedDescription='Sua fonte de notícias sobre o cantor e compositor Louis Tomlinson no Brasil! | Fan Account \nallofthosevoices.com', descriptionLinks=[TextLink(text='allofthosevoices.com', url='http://allofthosevoices.com', tcourl='https://t.co/qDuFir8dib', indices=(92, 115))], verified=False, created=datetime.datetime(2021, 11, 10, 0, 43, 46, tzinfo=datetime.timezone.utc), followersCount=2660, friendsCount=405, statusesCount=9308, favouritesCount=5406, listedCount=22, mediaCount=4572, location='', protected=False, link=TextLink(text='louist.lnk.to/FaithInTheFutu…', url='https://louist.lnk.to/FaithInTheFuture', tcourl='https://t.co/MXnvrVMPPC', indices=(0, 23)), profileImageUrl='https://pbs.twimg.com/profile_images/1625173839889022992/wt5_Zo9X_normal.jpg', profileBannerUrl='https://pbs.twimg.com/profile_banners/1458233634708672518/1676306614', label=None), replyCount=239, retweetCount=7, likeCount=259, quoteCount=393, conversationId=1630305816359084034, lang='pt', source='<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', sourceUrl='http://twitter.com/download/android', sourceLabel='Twitter for Android', links=None, media=[Photo(previewUrl='https://pbs.twimg.com/media/FqACgAPWAAA2DSV?format=jpg&name=small', fullUrl='https://pbs.twimg.com/media/FqACgAPWAAA2DSV?format=jpg&name=orig', altText=None)], retweetedTweet=None, quotedTweet=None, inReplyToTweetId=None, inReplyToUser=None, mentionedUsers=None, coordinates=None, place=None, hashtags=None, cashtags=None, card=None, viewCount=38830, vibe=None)), 
    ('inReplyToTweetId', None), 
    ('inReplyToUser', None), 
    ('mentionedUsers', None), 
    ('coordinates', None), 
    ('place', None), 
    ('hashtags', None), 
    ('cashtags', None), 
    ('card', None), 
    ('viewCount', 115), 
    ('vibe', None)])
    """
    #break
    
    
    if len(tweets) == limit:
        break
    else: #revisar origen de tweet y cantidad de tweet > 2700
        tweets.append([tweet.id, tweet.date, tweet.user.username, tweet.content, tweet.lang, TextBlob(tweet.content).sentiment])

df = pd.DataFrame(tweets, columns = ['ID', 'Date', 'User', 'Tweet', 'Language', 'SentimentAnalysis'])
#print(df.dtypes) #data types
#print(df.shape) #number of rows and columns
#print(df.columns) #name of columns

#The score in a sentiment analysis result represents the intensity or strength of the sentiment. It is not a confidence score. 
#This score is always a value in the range [-1, 1]. A score below -0.3 indicates a negative (sad/angry) sentiment, 
#while a score above 0.3 indicates a positive (joyful/happy) sentiment. Scores in the range [-0.3, 0.3] indicate neutral sentiment.
#print(df[['Tweet']])
print(df)

