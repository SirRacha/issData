from requests import get as geturl
url = 'http://api.open-notify.org/iss-now.json'
response = geturl(url)
result = response.json()
print(result)

git commit

This is a new file
