import tweepy
import pandas as pd

consumer_key = "uUAwjTFtvZ57VBayknHUqedYV"
consumer_secret = "tG23IDzGgUt8zRqEzKWJ1wWyBs4Cozx040DgynINpycLU1Ix4E"
access_token = "1376278105-k6zsXudNd3UVyX2VZlZq9iSyplHWDHkB7PdZ9IG"
access_token_secret = "j2EVBlKcyoxxueJdB2FTrJM05rOZakYU8nfcpkcUGsiI2"
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
number_of_items=500

searchword="#COVID and #DELHI "
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])


searchword="#COVID and #Chennai"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df1=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Mumbai"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df2=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Bengaluru"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df3=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

searchword="#COVID and #Kolkata"
tweets=tweepy.Cursor(api.search,q=searchword,lang='en').items(number_of_items)
names_text=[[tweet.user.screen_name,tweet.text.lower(),tweet.created_at,tweet.user.location.lower()]for tweet in tweets]
df4=pd.DataFrame(data=names_text,columns=['Name','Text',"Date","Location"])

frames=[df,df1,df2,df3,df4]
result = pd.concat(frames)
print(result)


for i in range(len(result)) :
    if "delhi" in result.iloc[i, 3] or "delhi" in result.iloc[i, 1]:
        result.iloc[i, 3]="Delhi"
    elif "mumbai" in result.iloc[i, 3] or "mumbai" in result.iloc[i, 1]:
        result.iloc[i, 3]="Mumbai"
    elif "chennai" in result.iloc[i, 3] or "chennai" in result.iloc[i, 1]:
        result.iloc[i, 3]="Chennai"
    elif "bengaluru" in result.iloc[i, 3] or "bengaluru" in result.iloc[i, 1]:
        result.iloc[i, 3]="Bengaluru"
    elif "kolkata" in result.iloc[i, 3] or "kolkata" in result.iloc[i, 1]:
        result.iloc[i, 3] = "Kolkata"
    else:
        result.iloc[i, 3] = "Other"


result.to_csv('tweets.csv', index=False)
