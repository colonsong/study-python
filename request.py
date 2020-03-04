import requests

url = 'https://api.exchangerate-api.com/v4/latest/TWD'  #以TWD為基準
res = requests.get(url)
data = res.json()
print(data['rates'])
