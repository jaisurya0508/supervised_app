import requests

url = 'http://localhost:5000/validate'
r = requests.post(url,json={'age':30, 'weight':60})

print(r.json())



url = 'http://localhost:5000/validates'
r = requests.post(url,json={'Kilometer':56})

print(r.json())