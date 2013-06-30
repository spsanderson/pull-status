import urllib
import json

response = urllib.urlopen(
    "http://search.twitter.com/search.json?q=microsoft"
)
pyresponse = json.load(response, encoding="utf-8")
# type(pyresponse) = 'dict' This denotes it as a dictionary where 
# results can be obtained using something like pyresponse.keys() which 
# will give a list of the keys in the pyresponse dictionary
print "pyresponse is a " + str(type(pyresponse))
print "the pyresponse keys are " + str(pyresponse.keys())
print ''
# pyresults is a list of dictionary keys
pyresults = pyresponse["results"]
print pyresults[0]['text']

for i in range(10):
	print pyresults[i]['text']
