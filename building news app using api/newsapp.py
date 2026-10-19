import requests 

query = input ("enter the news you want to read?")

api = "pub_b2d62b63bf6047dabd4af66243b0202d"


news = f"https://newsdata.io/api/1/latest?apikey={api}&q={query}&prioritydomain=top"

print(news)

r = requests.get(news)

data = r.json()

articla = data["results"]

for i in articla:
    print(i["title"])
    print("-"*20)