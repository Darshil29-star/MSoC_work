import requests

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text

text_data = text_data[:1000]
print(text_data)