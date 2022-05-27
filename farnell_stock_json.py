import requests

# Making a get request

def get_farnell_stock_qty(part_number):

 
    url = "https://api.element14.com/catalog/products?versionNumber=1.2&term=id%3A"
    url = url + part_number
    url = url + "&storeInfo.id=uk.farnell.com&resultsSettings.offset=0&resultsSettings.numberOfResults=1&resultsSettings.refinements.filters=rohsCompliant%2CinStock&resultsSettings.responseGroup=large&callInfo.omitXmlSchema=false&callInfo.responseDataFormat=json&callinfo.apiKey=rhcf7dupd8arzxtvqubksbbw"
    response = requests.get(url)
    data = response.json()
    print(data['premierFarnellPartNumberReturn']['products'][0]['stock']['level']) # 
    

get_farnell_stock_qty("1562051")