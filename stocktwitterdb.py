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
        stream.filter(track=['$ATVI','#ATVI','activision','$ADBE','#ADBE','Adobe','$AKAM','#AKAM','Akamai','$ALXN',
                             '#ALXN','alexion','$ALTR','#ALTR','altera','$AMZN','#AMZN','amazon.com','$AMGN','#AMGN',
                             'amgen','$APOL','#APOL','apollo group','$AAPL','#AAPL','apple','$AMAT','#AMAT','Applied materials',
                             '$ADSK','#ADSK','Autodesk','$ADP','#ADP','Automatic Data Processing','$AVGO','#AVGO',
                             'avago technologies','$BIDU','#BIDU','Baidu','$BBBY','#BBBY','Bed Bath and Beyond','Bed Bath & Beyond',
                             '$BIIB','#BIIB','Biogen','$BMC','#BMC','BMC Software','$BRCM','#BRCM','Broadcom',
                             '$CHRW','#CHRW','C.H. Robinson Worldwide','$CA','#CA','CA Inc','$CELG','#CELG','Celgene Corporation',
                             '$CERN','#CERN','Cerner Corporation','$CHKP','#CHKP','Check Point Software Technologies',
                             '$CSCO','#CSCO','Cisco','$CTXS','#CTXS','Citrix Systems','$CTSH','#CTSH','Cognizant Technology Solutions',
                             '$CMCSA','#CMCSA','Comcast','$COST','#COST','Costco','$DELL','#DELL','Dell','$XRAY','#XRAY','Dentsply',
                             '$DTV','#DTV','Direct TV','$DLTR','#DLTR','Dollar Tree','$EBAY','#EBAY','eBay','$ERTS','#ERTS',
                             'Electronic Arts','EA','$EXPE','#EXPE','Expedia','$EXPD','#EXPD','Expeditors International of Washington',
                             '$ESRX','#ESRX','Express Scripts','$FFIV','#FFIV','F5 Networks','$FAST','#FAST','Fastenal Company',
                             '$FISV','#FSIV','Fiserv','$FLEX','#FLEX','Flextronics','$FOSL','#FOSL','Fossil Inc.','$GRMN','#GRMN',
                             'Garmin','$GILD','#GILD','Gilead Inc','$GOOG','#GOOG','Google'])
