import requests

r = requests.get('https://www.washingtonpost.com/arcio/news-sitemap/')
print(r.content)