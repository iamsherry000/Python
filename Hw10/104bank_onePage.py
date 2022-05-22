# Application 104 bank (one page only)

import requests
import bs4

url = 'https://www.104.com.tw/jobs/search/?keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0'

htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
jobs = objSoup.find_all('article',class_ = 'js-job-item')
n=1
for job in jobs:
    print("編號: ",n)
    print("公司名稱: ",job.get('data-cust-name'))
    print("職務名稱: ",job.get('data-job-name'))
    n+=1