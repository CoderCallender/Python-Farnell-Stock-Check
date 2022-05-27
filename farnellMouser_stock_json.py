import requests
import json
import urllib
import httplib2

class part:
  part_number = 0
  stock_level = 0
  manu_part_number = ""
  details = ""

#https://api.mouser.com/api/v1/search/partnumber?apiKey=e14b0550-62b2-4a23-8d54-04a3c58a960b

def get_mouser_data(part_number):

    my_url = 'https://api.mouser.com/api/v1.0/search/'
    my_url += part_number
    my_url += '?apiKey=e14b0550-62b2-4a23-8d54-04a3c58a960b'

    #print(url)
    inputs = ": {    \"mouserPartNumber\": \"80-CKC18C103JDGCAUTO\",    \"partSearchOptions\": \"5\"  }}"
    headers =  {"accept": "application/json","Content-Type":"text/json"}
    #response = requests.post(url, json=inputs)
    response = requests.post(url = my_url, data=inputs, headers=headers, timeout=2.50)
 #   response = requests.get(url)   #get the data from the web
 #   data = json.loads(response.text)                                       #load it into a variable
    print(response.json())

  #  part.part_number = data['premierFarnellPartNumberReturn']['products'][0]['sku']
  #  part.stock_level = data['premierFarnellPartNumberReturn']['products'][0]['inv']
 #   part.manu_part_number = data['premierFarnellPartNumberReturn']['products'][0]['translatedManufacturerPartNumber']
 #   part.details = data['premierFarnellPartNumberReturn']['products'][0]['displayName']

def get_farnell_data(part_number):

    url = 'https://api.element14.com/catalog/products?versionNumber=1.2&term=id%3A'
    url += part_number
    url += '&storeInfo.id=uk.farnell.com&resultsSettings.offset=0&resultsSettings.numberOfResults=1&resultsSettings.refinements.filters=rohsCompliant%2CinStock&resultsSettings.responseGroup=large&callInfo.omitXmlSchema=false&callInfo.responseDataFormat=json&callinfo.apiKey=rhcf7dupd8arzxtvqubksbbw'

    #print(url)

    response = requests.get(url)   #get the data from the web
    data = json.loads(response.text)                                       #load it into a variable

    part.part_number = data['premierFarnellPartNumberReturn']['products'][0]['sku']
    part.stock_level = data['premierFarnellPartNumberReturn']['products'][0]['inv']
    part.manu_part_number = data['premierFarnellPartNumberReturn']['products'][0]['translatedManufacturerPartNumber']
    part.details = data['premierFarnellPartNumberReturn']['products'][0]['displayName']




part_info = part()  #init the class
get_farnell_data("2895628")
print(part_info.details)
print(part_info.stock_level)
#get_mouser_data("80-CKC18C103JDGCAUTO")
