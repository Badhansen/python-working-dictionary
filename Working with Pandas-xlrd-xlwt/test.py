from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListeneer

ckey = 'VEuLeWINSwHhUAIvybvPereiO'
csecret = 'Juy60kUyeJ6Fyl2tKcACotbfhvnR4gmCyI9lANlV8EQrbKmmQy'
atoken = '968707349698531338-nZsqcPTn1YnUUlD0ymOGEig4e1B4ZG8'
asecret = 'ILXwJO3ZDTvWkBezuHzjcQC74NQMAFbmwsgrYyrQCtwGo'

class listener(StreamListener):

    def on_data(self, data):

        print(data)
        return True
    def on_error(self, status):
        print(status)



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listner())
twitterStream.filter(track=["car"])
