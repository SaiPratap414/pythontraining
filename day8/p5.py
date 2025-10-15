import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
for data in res:
    print(data)