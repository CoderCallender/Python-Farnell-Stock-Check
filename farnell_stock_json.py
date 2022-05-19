import requests

# Making a get request
response = requests.get('https://api.element14.com/catalog/products?versionNumber=1.2&term=id%3A1652963&storeInfo.id=uk.farnell.com&resultsSettings.offset=0&resultsSettings.numberOfResults=1&resultsSettings.refinements.filters=rohsCompliant%2CinStock&resultsSettings.responseGroup=large&callInfo.omitXmlSchema=false&callInfo.responseDataFormat=xml&callinfo.apiKey=rhcf7dupd8arzxtvqubksbbw')
data = response.json()
print(type(data.inv)) # <class 'dict'>