import urllib.request
import os

def download_web_image(url):
    file_name = name + ".jpg"
    full_name = os.path.join(path, file_name)
    urllib.request.urlretrieve(url, full_name)

path = "/home/jszymkie/Desktop/PYPRO/images"
name = "gil"
url = "https://github.com/joeszym/ENEE_408I_Spring2021_images/blob/main/" + name + ".jpg?raw=true"
download_web_image(url)
