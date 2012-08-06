import time
import MySQLdb
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="# consumer_key here"
consumer_secret="# consumer_secret here"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="# access_token here"
access_token_secret="# access_token_secret here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

class StdOutListener(StreamListener):
        """ A listener handles tweets are the received from the stream.
        This is a basic listener that just prints received tweets to stdout.

        """
        def on_data(self, data):
            #print data
            #thedict = ast.literal_eval(data)
            null=''
            true=True
            false=False
            thedict = eval(data)
            print thedict['text']
            return True

        def on_error(self, status):
            print status

if __name__ == '__main__':
        l = StdOutListener()

        stream = Stream(auth, l)	
        stream.filter(track=['$MSFT','$GOOG','$CSCO','$AAPL','$C','$BA'])
