from __future__ import division
import sys
import json
import re


def main():

    f = file(sys.argv[1], "r")
    lines = f.readlines()
    cnt = 0;
    words = {}
    get = words.get
    for line in lines:
        tweet = json.loads(line)
        if tweet.has_key("text") and tweet["text"]:
            text = tweet["text"]
            twi_text = text.encode('utf-8') 
            twi_words = [e.strip() for e in twi_text.split() if len(e) >= 2]
            for word in twi_words:
                cnt = cnt + 1
                words[word] = get(word, 0) + 1

    for key,val in words.items():
        if key:
            try: 
                w1 = key.encode('utf-8')
            except: continue
            print '%s\t%.7f' % (w1, val/cnt)
    
if __name__ == '__main__':
    main(


    )
