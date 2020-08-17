# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_742235.html")
soup = BeautifulSoup(fhand, "html.parser")

count = 0
spa = soup('span')
for span in spa:
    line = span.contents[0]
    #print(line)
    line = int(line)
    count = count + line
print(count)


    
    