import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
response = requests.get(url)

with open("german_credit.data", "wb") as file:
    file.write(response.content)

print("Download complete")