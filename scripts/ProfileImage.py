import requests
import urllib.parse
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import re, sys

def image(url, username):
    session = requests.session()
    #header parameter is used to resolve the bad gateway 502 error
    #html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

    #opening the URL and parsing it into BeautifulSoup
    try:
        html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    except:
        print("Page not found or No internet connection")
        sys.exit()

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('body')

    #using regular expression to extract the image URL
    try:
        profile_pic_url_hd = re.findall(r"profile_pic_url_hd\":\"([\S]+?)\"",str(tags[0]))[0].replace(r'\u0026', '&')
        return profile_pic_url_hd
    except IndexError:
        return None
