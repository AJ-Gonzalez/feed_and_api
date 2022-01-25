import requests

url = 'http://127.0.0.1:5000/addmovie'
myobj = {"title": "Example title",
         "price": 6,
         "description": "A sample movie",
         "release": "Jan 1990"}

x = requests.post(url, data=myobj)

print(x.text)
