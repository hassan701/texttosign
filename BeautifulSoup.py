from bs4 import BeautifulSoup
import requests
import urllib.request

url = "https://www.signasl.org/sign/"

response = requests.get(url,data="help")


soup = BeautifulSoup(response.content, 'lxml')

container = soup.find('div',class_='video-js vjs-default-skin vjs-paused vjs-controls-enabled vjs-user-inactive')
print(container.prettify())

images = soup.find_all("img", attrs = {"alt": "Post image"})

""" number = 0
for image in images:
    image_src = image["src"]
    urllib.request.urlretrive(image_src, str(number))
    number +=1
     """
    
    