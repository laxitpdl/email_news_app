import requests

api_key = '5a3f08b0214d4717a7333e090cb30be4'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2025-12-06&sortBy=publishedAt&apiKey=5a3f08b0214d4717a7333e090cb30be4'
    
request = requests.get(url)      # .get talks to backend api
content = request.json()    #.json converts json to python!

for article in content ["articles"]:
   print(article["title"])