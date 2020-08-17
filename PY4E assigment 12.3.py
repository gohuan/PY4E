# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input("Count:"))
pos = int(input("Position:"))
url = input("Enter:")
html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Fikret.html"'''url''', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = list()

for thing in range(0,count):
    tags = soup('a')
    tag = tags[pos-1]
    need = tag.get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(tag.get('href', None))