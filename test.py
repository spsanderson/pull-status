#Importing the modules
import urllib2
import json
 
#Ask search query
query = raw_input("Please enter a query: ")

#Prints the search string
print query

#The actual query
url = "http://search.twitter.com/search.json?q=" + query
request = urllib2.Request(url)
response = json.load(urllib2.urlopen(request))

# Print out the keys to the response file
print "The response keys are: " + str(response.keys())
print ''

# Put the 'results' key in a variable
testresults = response['results']

# Print out the keys to the testresults file
print "The testresults keys are: " + str(testresults[0].keys())
print ''
print testresults[0]['text']
print ''
# print json.dumps(response,indent=2)
# the above line prints the entire json file
