#from pyblog import BlogError
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import MySQLdb
import mysql.connector
from mysql.connector import errorcode
import time
import datetime
import json



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.

conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'test'
        )
c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey="vQxgJthaTuiBVxni1GN9krvBR"
csecret="I2g6jU2VwWMfQkAZoe3mOlNIs02Z3ZT9Sfu2LIXk41rfjfDbhX"
atoken="2594541058-mHI2NIRXDoPPWlfDeBP0WqDMXUrBoUhmyq9Xg0H"
asecret="mONEajknkYkEXnevyEsFAw252ZkxJb6L4VmEN3qumFqGZ"

i=0
class listener(StreamListener):

    def on_data(self, data):
        global i # it's a global variable different from other language
        i+=1
        if(i<200000):#for limitting streaming tweets
            all_data = json.loads(data)

            tweet = all_data["text"]

            username = all_data["user"]["screen_name"]

            c.execute("INSERT INTO training (time, username, tweets) VALUES (%s,%s,%s)",
                        (time.time(), username, tweet))

            conn.commit()
            print(tweet)
            print(i)

            return True
        else:
            return False

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
#twitterStream.filter(languages=["en"])
#twitterStream.filter(languages=["en"])
#,locations=[-180,-90,180,90]

twitterStream.filter(languages=["en"],track=["Bomb","against","smash","aggression",
"harm","shot","bust","strike","blast","explosions","attack",
"fire","killed","riot","clashes","violence","bombard","charge","terror","panic",
"explosive","destruction","destructive","missile","bullet","damage","demolish","destroy","injure",
"harass","disaster","assail","loot","rob","rifle","blade""pistol","clash","projectile",
"grenade","gunpower","burst","ruin","fire uppon","strike","bummer","flop","rout",
"wreck","destroy","break in","despoil","foray","sack","spoliate","torpedo",
"gun","battle","knife","musket","pistol","brawl"])

#twitterStream.filter(locations=[-122.5213430856905, 37.941878236229385, -122.3412509143095, 37.60606576377062])
