import requests
import json

user = input().split(',')
products = {'result': []}
brand = input()
for product in user:
    params = {
        'q': product,
        'root': 'search',
        'searchType': 'searchType',
        'sourcepage': 'Search+Page'
    }
    response = requests.get(url='https://www.nykaa.com/search/result/', params=params, headers={'Content-Type': 'application/json','Accept': 'application/json',
                                                         'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/46.0.2490.80'})


    start = response.text.find('"products":[{"addToCartUrl":')
    end = response.text.find('],"filterMap":')
    c = response.text[start:end+1]
    d = c[11:]
    e = json.loads(d)

    q=[]
    for i in e:
        q.append(i['brand_name'][0].lower())
    products['result'].append({'keyword': product,
                               'position': {
                                        brand: q.index(brand)
                               }})
print(products)
