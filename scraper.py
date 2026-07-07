import requests

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print("Response Oject  :", response)
print("Status Code     :", response.status_code)