import requests

r = requests.get('https://api.github.com/user')
print(r.status_code)