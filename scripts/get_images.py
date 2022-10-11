from bs4 import BeautifulSoup
from get_urls import image_urls

import requests
import urllib.request 
import time
import os

DATASET_DIR = '/'

#store the data 
images = []
names = []

#create soup object to parse image URLs from HTML page
def getURLs(url): 
    print(f"Requesting URL: {url}")  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') 
    image = 'https:' + soup.find('meta', itemprop='image').get('content')
    image = image.split('?', 1)
    image = image[0]
    images.append(image)
    name = soup.find('h1', itemprop='name').text
    name = name.split(' -', 1)
    name = name[0]
    names.append(name)
    print(f"Extracting image URL: {image}")

#loop through image URLs
for url in image_urls:
    getURLs(url)

#download the images with appropiate file names
for i, n in zip(images, names):
    urllib.request.urlretrieve(i, DATASET_DIR + n + str(time.time()) + '.jpg')
    print(f"Downloading image: {i}")




 
