import sys
import time
#import MySQLdb
import tweepy
import ast
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

class StdOutListener(StreamListener):
        """ A listener handles tweets are the received from the stream.
        This is a basic listener that just prints received tweets to stdout.

        """
        def on_status(self, data):
            try:
                print '%s , %s , %s , %s, s%' % (data.text,\
                data.author.screen_name,data.created_at,data.source,\
                data.coordinates)
                return True
            except Exception, e:
                print >> sys.stderr, 'Encountered Exception:', e
                pass

        def on_error(self, status):
            return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

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
                         'Garmin','$GILD','#GILD','Gilead Inc','$GOOG','#GOOG','Google','$GMCR','#GMCR','Green Mountain Coffee',
                         '$HSIC','#HSIC','Henry Schein','$INFY','#INFY','Infosys Limited','$INTC','#INTC','Intel Corporation',
                         'Intel','$INTU','#INTU','Intuit','$ISRG','#ISRG','Intuitive Surgical Inc','$KLAC','#KLAC','KLA-Tencor',
                         '$KFT','#KFT','Kraft','$LRCX','#LRCX','Lam Research','$LINTA','#LINTA','Liberty Media Corporation',
                         '$LIFE','#LIFE','Life Technologies Corporation','$LLTC','#LLTC','Linear Technology Corporation',
                         '$MRVL','#MRVL','Marvell Technology Group','$MAT','#MAT','Mattel','$MXIM','#MXIM',
                         'Maxim Integrated Products','$MCHP','#MCHP','Microchip Technology Incorporated','$MU','#MU',
                         'Micron Technology Inc.','$MSFT','#MSFT','Mircrosoft','$MNST','#MNST','Monster Beverage Corporation',
                         '$MYL','#MYL','Mylan Inc','$NTAP','#NTAP','NetApp Inc','$NFLX','#NFLX','Netflix','$NUAN','#NUAN','Nuance   Communications',
                         '$NVDA','#NVDA','NVIDIA','$NWSA','#NWSA','News Corporation','$ORLY','#ORLY',"O'Reilly Automotive",
                         '$ORCL','#ORCL','Oracle Corp','$PCAR','#PCAR','PACCAR Inc','$PAYX','#PAYX','Paychex Inc','$PCLN','#PCLN',
                         'priceline.com Inc','$PRGO','#PRGO','Perrigoo Company','$QCOM','#QCOM','QUALCOMM','$RIMM','#RIMM',
                         'Research in Motion','$ROST','#ROST','Ross Stores Inc','$SNDK','#SNDK','SanDisk Corporation','$STX','#STX',
                         'Seagate TEchnology','$SHLD','#SHLD','Sears Holdings Corporation','$SIAL','#SIAL','Sigma-Aldrich Corporation',
                         '$SIRI','#SIRI','Sirius XM Radio','$SPLS','#SPLS','Staples Inc','$SBUX','#SBUX','Starbucks','$SRCL','#SRCL',
                         'Stericycle Inc','$SYMC','#SYMC','Symantec Corporation','$TXN','#TXN','Texas Instruments','$VRSN',
                         '#VRSN','VeriSign','$VRTX','#VRTX','Vertex Pharmaceuticals','$VIAB','#VIAB','Viacom','$VMED',
                         '#VMED','Virgin Media Inc','$VOD','#VOD','Vodafone Group','$WCRX','#WCRX','Warner Chilcott',
                         '$WFM','#WFM','Whole Foods Market','$WYNN','#WYNN','Wynn Resorts','$XLNX','#XLNX','Xilinx Inc',
                         '$YHOO','#YHOO','Yahoo! Inc']) 
