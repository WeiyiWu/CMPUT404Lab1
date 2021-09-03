import requests
import os
print(requests.__version__)
print(requests.get('https://www.google.com/'))
#os.system("curl -i http://www.google.com/")
os.system('curl -o lab1.py https://raw.githubusercontent.com/WeiyiWu/CMPUT404Lab1/main/lab1.py')
os.system('curl https://raw.githubusercontent.com/WeiyiWu/CMPUT404Lab1/main/lab1.py')
