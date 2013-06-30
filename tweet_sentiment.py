import sys
import json


def main():

    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


# f is the output.txt file that is being used as the file that is being
# analyzed
    f = file(sys.argv[2], "r")
# lines gets each line of f that is to be analyzed
    lines = f.readlines()
# this for loop takes an index variable line inside of 'lines'
# it also says that a tweet is equal to json.loads(lines) and cnt
# is equal to 0 for now.
    for line in lines:
        tweet = json.loads(line)
        cnt = 0;
# Since we are using json.loads we know that each piece of the output
# file is a json dict so we want the 'text' portion of each twee
# or text = tweet["text"] and we want an if statement that takes
# if tweet.has_key("text")
        if tweet.has_key("text"):
            text = tweet["text"]
            # twi_text is the text portion of the tweet encoded in 
            # utf-8
            twi_text = text.encode('utf-8') 
            twi_words = [e.lower() for e in twi_text.split() if len(e) >= 2]
            for word in twi_words:
                a = [ val for key,val in scores.items() if key==word ]
                if a:
                    cnt = cnt + a[0]
        print '%.2f' % cnt

if __name__ == '__main__':
    main()
