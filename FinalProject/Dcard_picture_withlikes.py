#Load all URL images
import time
import requests,os
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
from fake_useragent import UserAgent
n=0

ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}

url = 'https://www.dcard.tw/f/meme'
html = requests.get(url,headers=headers)
html.encoding="UTF-8"

sp = BeautifulSoup(html.text,'html.parser')
#建立images月存圖片
images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links=sp.find_all('img')
for link in all_links:
#取 src 和 href 屬性内容
    src=link.get('src')
    href = link.get('href') #指定一個URL看連結要到哪
    attrs=[src,href]
    for attr in attrs:
#讀取 .jpg 和 .png檔
        if attr != None and ('.webp' in attr):
            full_path = attr
            filename= full_path.split('/')[-1]#取得圖檔名
            print(full_path)#儲存圖片
            try :
                headers = {'user-agent':ua.random}
                image = requests.get(full_path,headers=headers)
                f = open(images_dir + filename + str(n+1) + ".jpg", "wb")
                f.write(image.content)
                f.close()
                n+=1
            except:
                print("{}無法讀取!".format(filename))
#以下使用api獲取按讚數
#參考https://marketingliveincode.com/?p=5009
alldata = []
last_article = ''
a=[]
url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?popular=true&limit=10'
for i in range(5):
    if i != 0: # 判斷是否是第一次執行
        request_url = url +'&before='+ str(last_article)
    else:
        request_url = url # 第一次執行，不須加上後方的before
    headers = {'user-agent': ua.random}
    list_req = requests.get(request_url,headers=headers) # 請求
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    alldata.extend(getdata) # 將另一個陣列插在最後面
    
    last_article = getdata[-1]['id'] # 取出最後一篇文章
    print(last_article)
with open("test.txt","w+",encoding="UTF-8-sig")as f:
    for i in range(10):
        a.append(alldata[i]['likeCount'])
    print(a)
    f.write(str(a))