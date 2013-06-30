from __future__ import division
import sys
import json
import re

def point_in_poly(x,y,poly):
# http://geospatialpython.com/2011/08/point-in-polygon-2-on-line.html
   # check if point is a vertex
   if (x,y) in poly: return "IN"

   # check if point is on a boundary
   for i in range(len(poly)):
      p1 = None
      p2 = None
      if i==0:
         p1 = poly[0]
         p2 = poly[1]
      else:
         p1 = poly[i-1]
         p2 = poly[i]
      if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
         return "IN"
      
   n = len(poly)
   inside = False

   p1x,p1y = poly[0]
   for i in range(n+1):
      p2x,p2y = poly[i % n]
      if y > min(p1y,p2y):
         if y <= max(p1y,p2y):
            if x <= max(p1x,p2x):
               if p1y != p2y:
                  xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
               if p1x == p2x or x <= xints:
                  inside = not inside
      p1x,p1y = p2x,p2y

   if inside: return "IN"
   else: return "OUT"


def main():

    json_data=open("states.json")
    map = json.load(json_data)
    states = map["states"]["state"]
    readablemap = {}
    for state in states:
        point = state["point"]	
        name = state["-name"]
        print name
        poligono = [(float(coord["-lat"]), float(coord["-lng"])) for coord in point]	
        readablemap[name] = poligono


    scorecard = {}
    get = scorecard.get
    for state in readablemap:
        scorecard[state] = {}
        scorecard[state]["postot"] = 0
        scorecard[state]["poscnt"] = 0
        scorecard[state]["negtot"] = 0
        scorecard[state]["negcnt"] = 0

    afinnfile = open(sys.argv[1])
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    f = file(sys.argv[2], "r")
    lines = f.readlines()

    for line in lines:
        tweet = json.loads(line)
        if tweet.has_key("coordinates") and tweet["coordinates"]:
            if tweet.has_key("text") and tweet["text"]:
                text = tweet["coordinates"]["coordinates"]
                lon = tweet["coordinates"]["coordinates"][0]
                lat = tweet["coordinates"]["coordinates"][1]
                for state in readablemap:
                    if point_in_poly(lat, lon, readablemap[state]) == "IN":
                        text = tweet["text"]
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
    winner = ()
    for state in scorecard:
        cur_cnt = scorecard[state]["postot"] + scorecard[state]["negtot"]
        cur_cnt = scorecard[state]["postot"] + scorecard[state]["negtot"]
        if cur_cnt > runner:
            runner = cur_cnt
            winner = state
    #print winner
    
if __name__ == '__main__':
    main(


    )
