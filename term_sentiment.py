from __future__ import division
import sys
import json
import re

def main():
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    scorecard = scores.get
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # initialize newwords dict
    newdict = {}
    #newdict.update({"the":{'cnt': 0, 'tot': 0}})
    
    f = file(sys.argv[2], "r")
    lines = f.readlines()
    for line in lines:
        tweet = json.loads(line)
        cnt = 0
        b = []
        if tweet.has_key("text"):
            text = tweet["text"]
            if len(text) < 1: continue
            twi_text = text.encode('utf-8') 
            twi_words = [e.lower() for e in twi_text.split() if len(e) >= 2]
            for word in twi_words:
                word = word.strip()
                try: 
                    word += 1
                    continue
                except:                 
                    if "http" in word: continue
                    if '&' in word: continue
                    a = scorecard(word)
                    if a:
                        cnt = cnt +  a
                    else: 
                        b.append(word)
        else: continue
        if cnt:
            for newword in b:
                if newdict.get(newword, 0):
                    newdict[newword]["cnt"] = newdict[newword]["cnt"] + cnt
                    newdict[newword]["tot"] = newdict[newword]["tot"] + 1
                else:
                    newdict.update({newword:{'cnt': cnt, 'tot': 1}})


    for word in newdict:
        if newdict[word]["tot"] > 2:
            print '%s\t%.7f' % (word, newdict[word]["cnt"]/newdict[word]["tot"])   


if __name__ == '__main__':
    main()
