# Load a URL image
import requests,os
from urllib.request import urlopen

url = "https://web.mcu.edu.tw/sites/default/files/logo-img.png"

html = requests.get(url)
if html.status_code != requests.codes.ok:
    print("{} cannot read!".format(url))
else:
    print("can be readed.")
    images_dir="images/"
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
    filename = url.split('/')[-1]
    image = urlopen(url)
    f = open(os.path.join(images_dir,filename),'wb')
    f.write(image.read())
    f.close()    

