import requests

result = requests.get('https://en.wikipedia.org/robots.txt')


with open("robots.txt", "wb") as file:
    file.write(result.content)
