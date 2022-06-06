#Load all URL images with no likes
import time
import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from fake_useragent import UserAgent
n=0

ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
url = 'https://www.dcard.tw/f/meme'
html = requests.get(url,headers=headers)
html.encoding="UTF-8"

sp = BeautifulSoup(html.text,'html.parser')
#建立images存圖片
#images_dir="C:/Users/a0920/Desktop/images/"
images_dir ="D:/github/Python/FinalProject/images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links=sp.find_all('img')
for link in all_links:
#取 src 和 href 屬性内容
    src=link.get('src')
    href = link.get('href') #指定一個URL看連結要到哪
    attrs=[src,href]
    if n == 11:
        break
    for attr in attrs:
#讀取 .jpg 和 .png檔
        if attr != None and ('.webp' in attr):
            full_path = attr
            filename= full_path.split('/')[-1]#取得圖檔名
            print(full_path)
#儲存圖片
            try :
                image = requests.get(full_path,headers=headers)
                f = open(images_dir + filename + str(n) + ".jpg", "wb")
                f.write(image.content)
                f.close()
                n+=1
                
            except:
                print("{}無法讀取!".format(filename))
print(n)