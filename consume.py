import requests


req = requests.get("https://ohmanda.com/api/horoscope/libraad")
print(req.json())