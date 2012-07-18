import time
# import MySQLdb # also not currently used
import tweepy
# from textwrap import TextWrapper # not used currently
from getpass import getpass

# define the format for messages here to avoid repetition
OUT_STR = '''
Status : %(text)s
Author : %(author)s
Date/Time : %(date)s
Source : %(source)s
Geo : %(geo)s




-----------------------------------------------------------------------------




'''


class StockTweetListener(tweepy.StreamListener):
    def __init__(self, target):
        super(StockTweetListener, self).__init__();
        self.target = target
        # status_wrapper = TextWrapper(width=60, initial_indent=' ',
        #                             subsequent_indent=' ')
        # This isn't used in the current code. But, if you were going
        # to use it, you'd need to assign it to self.status_wrapper;
        # otherwise the variable would be local to this __init__ method
        # and inaccessible from anything else.


    def on_status(self, status):
        try:
            msg = OUT_STR % {
                'text': status.text,
                'author': status.author.screen_name,
                'date': status.created_at,
                'source': status.source,
                'geo': status.geo,
            }
            print msg
            self.target.write(msg)
            # use self.target here. self is one of the paramaters to this
            # method and refers to the object; because you assigned to its
            # .target attribute before, you can use it here.


        except UnicodeDecodeError:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            print "Record Skipped"

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'

def main():
    username = raw_input('Twitter username: ')
    password = getpass('Twitter password: ')
    stock = raw_input('Name of Stocks(comma seperated): ')
    stock_list = [u for u in stock.split(',')]
    follow_list = None # ??? you don't seem to define this variable

    # open results.txt here and name it f locally. once code flow leaves
    # the with statement, in this case only through an exception happening
    # that jumps you out of the while loop, the file will be closed.
    with open('results.txt', 'w') as f:
         while True:
             stream = tweepy.Stream(
                            username, password,
                            StockTweetListener(f), # passes the file to __init__
                                                   # as the "target" argument

                            timeout=None)
             stream.filter(follow_list, stock_list)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
