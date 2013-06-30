from __future__ import division
import sys
import json
import re


def main(): 

    statenames = ("AK", "AL", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MO", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY")
    scorecard = {}
    for item in statenames:
       scorecard[item] = {"poscnt":0,"negcnt":0,"postot":0,"negtot":0}

    
    afinnfile = open(sys.argv[1])
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    f = file(sys.argv[2], "r")
    lines = f.readlines()

    for line in lines:
        tweet = json.loads(line)
        if tweet.has_key("place") and tweet["place"]:
            text = tweet["place"]["full_name"]
            if ',' in text:
                twi_place = text.encode('utf-8')
            else: continue
            if len(twi_place) < 2 and "," not in twi_place:
               continue
            first, last  = twi_place.split(",") 
            last = last.strip()
            if last in scorecard:
               state = last
            else: continue
            text = tweet["text"]
            if len(text) < 1: continue
            twi_text = text.encode('utf-8') 
            twi_words = [e.strip() for e in twi_text.split() if len(e) >= 2]
            cnt = 0
            for word in twi_words:
                if "http" in word: continue
                if '&' in word: continue
                word = re.sub(r'[{}@"=.!,;?#:()*_^~o/]', '', word)
                word = word.strip("-").strip("'").strip()
                a = [ val for key,val in scores.items() if key==word ]
                if a:
                    cnt = cnt + a[0]

            if cnt > 0:
                scorecard[state]["poscnt"] = 1 + scorecard[state]["poscnt"]
                scorecard[state]["postot"] = cnt + scorecard[state]["postot"]
            if cnt < 0:
                scorecard[state]["negcnt"] = 1 + scorecard[state]["negcnt"]
                scorecard[state]["negtot"] = cnt + scorecard[state]["negtot"]


    runner = 0
    winner = "none"
    for state in scorecard:
        cur_cnt = scorecard[state]["postot"] + scorecard[state]["negtot"]
        if cur_cnt > runner:
            runner = cur_cnt
            winner = state
    print winner
    
if __name__ == '__main__':
    main(


    )
