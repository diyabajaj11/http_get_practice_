import requests

url=input("Enter any API url;")

try:
    response=requests.get(url)

    print("Status code:",response.status_code)
    print("Response Header:",response.headers)

    try:
        print("Response JSON:",response.json())
    except ValueError:
        print("Respons Text",response.text)

except requests.exceptions.RequestException as e:
    print("Error:",e)