import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Give url:\t")  # προσδιορισμός του url

if not url.startswith('https://'):
    url = 'https://' + url

print(url)

with requests.get(url) as response:
    # for key in response.headers:
    #    print(f"{key}, Value:{response.headers[key]}")
    print(f"Server: {response.headers.get('Server')}")

    print(f"Has cookies: {len(response.cookies) > 0}")

    for cookie in response.cookies:
        print(f"Name: {cookie.name}, Expires:{datetime.fromtimestamp(cookie.expires)}")
