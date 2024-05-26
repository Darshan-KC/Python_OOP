# Request module

# The request module is an HTTP library that enables the developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and make it possible to interact with APIs and web services.

import requests

# response = requests.get("https://www.google.com")
# print(response.text)

data = {
    'title' : "Test Post",
    'body' : "This is body",
    "userId" : 1,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.post(url,headers=headers,json=data)
print(response.text)