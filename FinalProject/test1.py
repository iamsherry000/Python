# Load all URL images
import requests,os
from urllib.request import *
from bs4 import BeautifulSoup
import json

# url = "https://www.dcard.tw/f/meme"
# html = requests.get(url)
# html.encoding = "utf-8"

'''
url=requests.get("https://www.dcard.tw/f/meme")
headers = { "Referer": "https://www.dcard.tw/", "User-Agent": "Mozilla/5.0" }
req = Request(url, headers=headers)
urllib.request.urlopen(req).get()
'''

# sc-d831dd0e-2 fAmxXK a

p = requests.Session()
url=requests.get("https://www.dcard.tw/f/meme")
soup = BeautifulSoup(url.text,"html.parser")
sel = soup.select("sc-d831dd0e-2 fAmxXK")

a=[]
for s in sel:
    a.append(s["href"])
url = "https://www.dcard.tw"+ a[2]

for k in range(0,10):
        post_data={
            "before":a[-1][9:18],
            "limit":"30",
            "popular":"true"
        }
        r = p.get("https://www.dcard.tw/_api/forums/meme/posts",params=post_data, headers = { "Referer": "https://www.dcard.tw/", "User-Agent": "Mozilla/5.0" })
        data2 = json.loads(r.text)
        for u in range(len(data2)):
            Temporary_url = "/f/meme/p/"+ str(data2[u]["id"]) + "-" + str(data2[u]["title"].replace(" ","-"))
            a.append(Temporary_url)
j=0 #為了印頁數
q=0 #為了印張數
for i in a[2:]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    #file.write("temperature is {} wet is {}%\n".format(temperature, humidity))
    test.write("第 {} 頁的URL為: {} \n".format(j,url))
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    # sel_jpg = soup.select("div.Post_content_NKEl9 div div div img.GalleryImage_image_3lGzO")
    sel_jpg = soup.select("data-post-list-viesed-cell-no div div div div div div img.GalleryImage_image_3lGzO")
    for c in sel_jpg:
        q+=1
        print("第",q,"張:",c["src"])
        test.write("%\n""第 {} 張: {} \n".format(q,c["src"])) 
        pic=requests.get(c["src"])
        img2 = pic.content
        pic_out = open("D:/github/Python/FinalProject/images"+str(q)+".png",'wb')
        pic_out.write(img2)
        pic_out.close()

test.close()
print("爬蟲結束")