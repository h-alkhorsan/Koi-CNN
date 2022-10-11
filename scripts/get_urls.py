from bs4 import BeautifulSoup
import requests
import re

page_urls = []
site_urls = []

#loop through site pages
pages = range(1, 10)
for i in pages:
    source = "https://cuttlebrookkoifarm.co.uk/collections/koi-for-sale-cuttlebrook-koi-farm?page={pagenumber}".format(pagenumber = i)
    page_urls.append(source)

#request url of each page and store it in soup object
for url in page_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for a in soup.findAll('a', href=True):
        site_urls.append("https://cuttlebrookkoifarm.co.uk{}".format(a['href'])) 

#pattern matching regex to find only URLs of the images 
regex = r'https://cuttlebrookkoifarm.co.uk/collections/koi-for-sale-cuttlebrook-koi-farm/products/?\w+-?\w+-\d\dcm-ref-\d+'

#find the regex matches
for i in site_urls:
    matches = re.findall(regex, str(site_urls))

image_urls = list(matches)
print("Image URLs have been saved")

