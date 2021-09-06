import requests
print(requests.__version__)
print(requests.get('https://www.google.com/'))

rawURL = 'https://raw.githubusercontent.com/WeiyiWu/CMPUT404Lab1/main/lab1.py'
r = requests.get(rawURL, allow_redirects=True)
# download python script
# resource: https://www.tutorialspoint.com/downloading-files-from-web-using-python
open('lab01.py', 'wb').write(r.content)
# print source code
print(r.text)

