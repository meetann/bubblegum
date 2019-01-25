mport  tweepy
import  sys
topic=sys.argv[1]
consumer_key='GsT66rEq08JFyg9GwZAC4skzf'
consumer_sec='gODQ4BPmZie9OrIGW2TYXT2JZo2gPlv5K2cMP8ZLtJY0Z2rBvK'
#  by using above keys  we are going to check auth handler 
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  here auth is token by consuker key and sec 
access_key='3382393334-LPCwbcZg0O3V3ZbGye1jrHP3KiidyjfNxWxwqBw'
secret_key='xKlV471Of3kSCCH7FX9EEjtFi9u3Zz5bCifKRkEsvkjh9'
#  connecting  data server  with  access and secret key  by using above token
print(dir(auth))
auth.set_access_token(access_key,secret_key)
#  connecting to twitter api with  token that is stored in auth
connected=tweepy.API(auth)

#  searching topics 
tweet=connected.search(topic,count=10)

f=open('/root/Desktop/python2019/data.txt','w+')   #  read 
for  j  in  tweet:
	f.write(j.text)
print  f.read()
f.close()
