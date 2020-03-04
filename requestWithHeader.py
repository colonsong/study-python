import requests


headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


url = 'https://api.exchangerate-api.com/v4/latest/TWD'  #以TWD為基準
res = requests.get(url, headers=headers)
data = res.json()
print(data['rates'])
