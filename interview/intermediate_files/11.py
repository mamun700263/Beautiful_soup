from bs4 import BeautifulSoup
import requests


url = "http://127.0.0.1:5500/Demo.html"


response = requests.get(url)

soup = ''
if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
else:
    print("Sorry page not Found", response.status_code)

#### ✅ **Searching for Elements**
#Use of .find('tagname')
title = soup.find('title')
print('title tag: ', title) # <title>BeautifulSoup Example Page</title>
print('text in side the title tag: ',title.text)#BeautifulSoup Example Page

#Use of .find('tagname',attribute)
intro = soup.find('p',id="intro")
print('"p" tag that has a id named "intro" ',intro) #<p id="intro">This is an example webpage containing different HTML elements.</p>



