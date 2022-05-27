import requests
api_url = "https://api.mouser.com/api/v1/search/80-CKC18C103JDGCAUTO?apiKey=e14b0550-62b2-4a23-8d54-04a3c58a960b"
response = requests.get(api_url)
print(response.json())