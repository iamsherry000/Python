# dcard_picture_def
# 先清空資料夾、多了評論數與標籤、變更圖片取名規則
# 圖片只會下載10張梗圖

# Load all URL images
import requests,os,glob
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

def dcard():
    s=0

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

    pc_files = glob.glob(images_dir+'*.jpg')#刪除資料夾內的圖片
    for pc_file in pc_files:
        try:
            os.remove(pc_file)
        except OSError as e:
            print(f"Error:{ e.strerror}")

    all_links=sp.find_all('img')
    for link in all_links:
    #取 src 和 href 屬性内容
        if s==11:
            break
        src=link.get('src')
        href = link.get('href') #指定一個URL看連結要到哪
        attrs=[src,href]
        for attr in attrs:
    #讀取 .jpg 和 .png檔
            if attr != None and ('.webp' in attr):
                full_path = attr
                filename= full_path.split('/')[-1]#取得圖檔名
                print(full_path)#儲存圖片
                if s!=0:
                    try :
                        headers = {'user-agent':ua.random}
                        image = requests.get(full_path,headers=headers)
                        f = open(images_dir + str(s)+".jpg", "wb")
                        f.write(image.content)
                        f.close()
                        #print("我是",s)
                    except:
                        print("{}無法讀取!".format(filename))
                s+=1
    #以下使用api獲取按讚數
    #參考https://marketingliveincode.com/?p=5009
    alldata = []
    last_article = ''
    likeCount=[]
    commentCount=[]
    topics={}
    url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?popular=true&limit=10'
    for i in range(5):
        if i != 0: # 判斷是否是第一次執行
            request_url = url +'&before='+ str(last_article)
        else:
            request_url = url # 第一次執行，不須加上後方的before
        ua = UserAgent()
        headers = {'user-agent': ua.random}
        list_req = requests.get(request_url,headers=headers) # 請求
        #將整個網站的程式碼爬下來
        getdata = json.loads(list_req.content)
        alldata.extend(getdata) # 將另一個陣列插在最後面
        last_article = getdata[-1]['id'] # 取出最後一篇文章
        time.sleep(5)

    for i in range(10):
        topicscount=len(alldata[i]['topics'])
        for j in range(topicscount):
            if alldata[i]['topics'][j] not in topics:
                topics[alldata[i]['topics'][j]]=[str(i)+".jpg"]
            else:
                topics[alldata[i]['topics'][j]].insert(-1,str(i)+".jpg")
    with open("test.txt","w+",encoding="UTF-8-sig")as f:
        for i in range(10):
            likeCount.append(alldata[i]['likeCount'])
        for i in range(10):
            commentCount.append(alldata[i]['commentCount'])
        print("likeCount:",likeCount)
        print("commentCount:",commentCount)
        print("topics:",topics)
        f.write(str(likeCount)+"\n")
        f.write(str(commentCount)+"\n")
        f.write(str(topics))
        
    return(likeCount,commentCount,topics)

