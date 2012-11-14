'''
Short program to scrape historical price/volume data from Yahoo Fianance.
into local CSV files that can be read and used by QSTK.  We gratefully 
acknowledge Yahoo for making this data available.

(c) 2012 by Lucena Research
'''

import urllib2
import urllib
import datetime
import sys
import os


def get_data(data_path, ls_symbols):

    #Create path if it doesn't exist
    if not (os.access(data_path, os.F_OK)):
        os.makedirs(data_path)

    #utils.clean_paths(data_path)   

    _now =datetime.datetime.now();
    miss_ctr=0; #Counts how many symbols we could get
    for symbol in ls_symbols:
        symbol_name = symbol
        if symbol[0] == '$':
            symbol = '^' + symbol[1:]

        symbol_data=list()
        #print "Getting " + str (symbol_name)
        
        try:
            params= urllib.urlencode ({'a':1, 'b':1, 'c':2000, 'd':_now.month, 'e':_now.day, 'f':_now.year, 's': str(symbol)})
            url_get= urllib2.urlopen("http://ichart.finance.yahoo.com/table.csv?%s" % params)
            
            header= url_get.readline()
            symbol_data.append (url_get.readline())
            while (len(symbol_data[-1]) > 0):
                symbol_data.append(url_get.readline())
            
            symbol_data.pop(-1) #The last element is going to be the string of length zero. We don't want to write that to file.
            #now writing data to file
            f= open (data_path + symbol_name + ".csv", 'w')
            
            #Writing the header
            f.write (header)
            
            while (len(symbol_data) > 0):
                f.write (symbol_data.pop(0))
             
            f.close();    
                        
        except urllib2.HTTPError:
            miss_ctr= miss_ctr+1
            print "Unable to fetch data for stock: " + str (symbol_name)
        except urllib2.URLError:
            print "URL Error for stock: " + str (symbol_name)
            
    print "All done. Got " + str (len(ls_symbols) - miss_ctr) + " stocks. Could not get " + str (miss_ctr) + " stocks."   

def read_symbols(s_symbols_file):

    ls_symbols=[]
    file = open(s_symbols_file, 'r')
    for f in file.readlines():
        j = f[:-1]
        ls_symbols.append(j)
    file.close()
    
    return ls_symbols  

def main():
    path = './'
    ls_symbols = read_symbols('symbols.txt')
    get_data(path, ls_symbols)

if __name__ == '__main__':
    main()
