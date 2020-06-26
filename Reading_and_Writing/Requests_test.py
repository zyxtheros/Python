# Examples for usage of the requests library

import requests

myParams = {"q": "pizza"}
r = requests.get("https://bing.com", params= myParams)

print("status:", r.status_code)

print(r.url)
# print(r.text)

f = open("./page.html", "w+")
f.write(r.text) 