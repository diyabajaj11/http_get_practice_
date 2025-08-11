import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response=requests.get(url)

print("status code:",response.status_code)
print("Response JSON:",response.json())

