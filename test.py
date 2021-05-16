import requests
import json

url = "https://instagram47.p.rapidapi.com/user_posts"

querystring = {"username":"sasha_tsepilova"}

headers = {
    'x-rapidapi-key': "c2480c722emsh51bc692f9b351bcp1a170ajsnb495557dbedf",
    'x-rapidapi-host': "instagram47.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

js = response.json()
# print(js)

with open('file.json', 'w', encoding = 'utf-8') as files:
        json.dump(response.json(), files, indent = 4, ensure_ascii = False)


actual_imgsurls = []

body = js['body']
items = body['items'] #list

for ind in range(len(items)):
    for key in items[ind]:
        if key == 'image_versions2':
            cands = key['candidates']
            print(cands)
            one_elem = cands[0]
            print(one_elem)
            actual_imgsurls.append(one_elem['url'])

print(actual_imgsurls)

