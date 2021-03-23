import urllib.request
import os

def download_web_image(url):
    file_name = os.path.join(path, name)
    urllib.request.urlretrieve(url, file_name)

path = "/home/jszymkie/Desktop/PYPRO/images"
name = "gil.jpeg"
url = "https://github.com/UMD-ENEE408I/ENEE408I_Spring_2021_Team_5/blob/main/Image/" + name + "?raw=true"
download_web_image(url)
