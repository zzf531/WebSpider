import requests

r = requests.get('http://localhost:8080/tt')
print(r.text)