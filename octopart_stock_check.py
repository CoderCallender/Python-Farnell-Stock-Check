import json
import urllib

url = 'http://octopart.com/api/v3/parts/match?'
url += '&queries=[{"mpn":"SN74S74N"}]'
url += '&apikey=739d6ec0-35b5-4bb5-bc64-fbc4753656ca'

print(url)
#data = urllib.urlopen(url).read()
#response = json.loads(data)

# print request time (in milliseconds)
#print response['msec']

# print mpn's
#for result in response['results']:
#    for item in result['items']:
#        print item['mpn']
