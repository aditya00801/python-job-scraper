import requests

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print("Status Code :", response.status_code)
print("URL         :", response.url)
print("Encoding    :", response.encoding)
print("Headers     :", response.headers)
print("Text        :", response.text[:100])