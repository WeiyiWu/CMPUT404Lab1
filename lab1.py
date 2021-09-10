import requests
# print library version
print(requests.__version__)

# get Google homepage
print(requests.get('https://www.google.com/'))

# download python script
rawURL = 'https://raw.githubusercontent.com/WeiyiWu/CMPUT404Lab1/main/lab1.py'
r = requests.get(rawURL, allow_redirects=True)
# print source code
print(r.text)

