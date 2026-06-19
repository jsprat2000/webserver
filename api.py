import requests
from bs4 import BeautifulSoup

## testing http requests to small webserver

response = requests.get('http://localhost:8080/LocalPkt')

print(response.status_code)
print(response.text)