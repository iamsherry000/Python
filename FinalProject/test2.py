from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen

 
url=requests.get("https://www.dcard.tw/f/meme")
soup = BeautifulSoup(url.text, "lxml")
'''
html = requests.get(url)
html.encoding = "utf-8" 
'''

# results = soup.find_all(["img", {"class": "sc-d831dd0e-2 fAmxXK"}], limit=5)
 
all_links = soup.find_all("img", {"class": "sc-d831dd0e-2 fAmxXK"})
 

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