import time
import html5lib
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.google.com'

def goto_url(url):
    #time.sleep(1)
    return BeautifulSoup(urllib.request.urlopen(url),'lxml')

def get_url(soup):
    urls = {""}
    for comp in soup.find_all('a',href=True):
        urls.add(comp['href'])
    return urls

soups = goto_url(url)

all_url = get_url(soups)

print(all_url)
complete_url = all_url.copy()
long = all_url.__len__()
for urli in all_url:
    try:
        complete_url.add(get_url(goto_url(urli)))
    except:
        try:
            complete_url.add(get_url(goto_url(url+urli)))
        except:
            pass
    finally:
        long = long - 1
        print(long)

for i in complete_url:
    count=0
    for z in i.split("."):
        if z == "google":
            count = 1
        else:
            pass
    if count == 0:
        print(url+i)
    else:
        print(i)

def save_html(html,path):
    with open(path,'wb') as f:
        f.write(html)

def open_html(path):
    with open(path,'rb') as f:
        return f.read()
