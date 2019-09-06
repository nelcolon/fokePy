import requests
from bs4 import BeautifulSoup
import re
import urllib.request as request

def verify_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find(id="title").getText()
        print("Downloading: {} ".format(title))
        downloadSong(soup,title)
    except:
        print("Explotamos billy.")


def downloadSong(link,name):
    download_link = link.find("a", class_="btn")
    if download_link is not None:
        request.urlretrieve(download_link['href'], filename=name)
        


#Get page
try:
    url = 'http://alofokemusic.net/musica/'
    response = requests.get(url)
except:
    print("Couldn't get the URL")

#Parses the page to BS4 and once parsed, tries to find all music links in page. Then magic. It finds the 
try:
    soup = BeautifulSoup(response.text, "html.parser")
    #Pattern to look for only songs link
    pat = 'http://alofokemusic.net/musica/\d+/'
    elements = soup.find_all('a')
    
    final_links = []

    for ele in elements:
        element_link = ele.get('href')
        if element_link is not None and re.match(pat, element_link) :
            final_links.append(ele.get('href'))
except:
    print("Couldn't soupify html response")

for link in final_links:
    verify_url(link)