# Load all URL images
import requests,os
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/meme"
html = requests.get(url)
html.encoding = "utf-8"

sp = BeautifulSoup(html.text,'html.parser')

# 建立 images 目錄並儲存
images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# get all label <a> & <img> 
all_links = sp.find_all(['a','img'])
for link in all_links:
    # 讀取 src 和 href 屬性內容
    src = link.get('src')
    href = link.get('href') # 指定一個url看連結連到哪邊
    attrs = [src,href]
    for attr in attrs:
        # 讀取 .jpg 和 .png 檔案
        if attr != None and('.jpg' in attr or '.png' in attr):
            full_path = attr
            filename = full_path.split('/')[-1] # 取得圖檔名
            print(full_path)
            # save image
            try:
                image = urlopen(full_path)
                f = open(os.path.join(images_dir,filename),'wb')
                f.write(image.read())
                f.close()
            except:
                print("{} cannot read.".format(filename))