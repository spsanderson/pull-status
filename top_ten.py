from __future__ import division
import sys
import json
import re
import heapq

def main():

    f = file(sys.argv[1], "r")
    lines = f.readlines()
    cnt = 0
    words = {}
    get = words.get
    runner = 0
    for line in lines:
        tweet = json.loads(line)
        if tweet.has_key("entities") and tweet["entities"]["hashtags"]:
            hashes = tweet["entities"]["hashtags"]
            l = len(hashes)
            i  = 0 
            while i < l:
                hash = hashes[i]["text"].encode('utf-8') 
                i = i+1
                cur_cnt = get(hash, 0) + 1
                words[hash] = cur_cnt
                if cur_cnt > runner:
                    runner = cur_cnt
                    winner = hash                

    list = heapq.nlargest(10, words, key=words.get)
    i = 0
    while i < 10:
        print "%s\t%.7f" % (list[i], get(list[i], 1)) 
        i = i +1


    
if __name__ == '__main__':
    main(


    )
