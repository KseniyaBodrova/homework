import requests
from datetime import datetime

start = datetime.now()
response = requests.get('https://www.airandspaceforces.com/lockheed-tech-f-35-ccas/')
print(response)
end = datetime.now()
print(end - start)

