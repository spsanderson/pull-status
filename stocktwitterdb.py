from textwrap import TextWrapper

from getpass import getpass



qParam = "Twitter"



target = open('results.txt', 'w')

target.truncate()



def debug_print(text):

    """Print text if debugging mode is on"""

    if settings.debug:

        print text



class StockTweetListener(tweepy.StreamListener):



    status_wrapper = TextWrapper(width=60, initial_indent=' ', subsequent_indent=' ')



    def on_status(self, status):

        try:

            # print 'Status : %s' %(self.status_wrapper.fill(status.text))

            print '\nStatus : %s' %(status.text)            

            print '\nAuthor : %s' %(status.author.screen_name)

            print '\nDate/Time : %s' %(status.created_at)

            print '\nSource : %s' %(status.source)           

            print '\nGeo : %s' %(status.geo)

            print '\n\n\n-----------------------------------------------------------------------------\n\n\n'



            l1 = '\nStatus : %s' %(status.text)            

            l2 = '\nAuthor : %s' %(status.author.screen_name)

            l3 = '\nDate/Time : %s' %(status.created_at)

            l4 = '\nSource : %s' %(status.source)           

            l5 = '\nGeo : %s' %(status.geo)

            l6 = '\n\n\n-----------------------------------------------------------------------------\n\n\n'



            target.write(l1)

            target.write(l2)

            target.write(l3)

            target.write(l4)

            target.write(l5)

            target.write(l6)                                    

            

        except:

            # Catch any unicode errors while printing to console

            # and just ignore them to avoid breaking application.

            pass



    def on_error(self, status_code):

        print 'An error has occured! Status code = %s' % status_code

        target.close()

        return True # keep stream alive



    def on_timeout(self):

        print 'Snoozing Zzzzzz'

        target.close()



        







def main():

    username = raw_input('Twitter username: ')

    password = getpass('Twitter password: ')

    stock = raw_input('Name of Stocks(comma seperated): ')

    stock_list = [u for u in stock.split(',')]





    

    

    while 1:

        stream = tweepy.Stream(username,password, StockTweetListener(), timeout=None)

        follow_list = None

        stream.filter(follow_list,stock_list)







if __name__ == '__main__':

    try:

        main()

    except KeyboardInterrupt:

        target.close()

        quit()
