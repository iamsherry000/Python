# Application 104 bank (three pages)

import requests
import bs4
import random
import time
import csv

def job_list(url):
    global company_job
    global n
    htmlFile = requests.get(url)
    objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
    jobs = objSoup.find_all('article',class_ = 'js-job-item')
    for job in jobs:
        company_name = job.get('data-cust-name')
        job_name = job.get('data-job-name')
        dict1={"編號":n,"公司名稱":company_name,"職務名稱":job_name}
        print("公司名稱: ",company_name)
        print("職務名稱: ",job_name)
        company_job.append(dict1)
        n=n+1
        if n == 101:
            break

def write_to_csv():  #  save data to csv file
    f_name = "104_software_Engineering.csv"  # save file name
    with open(f_name,"w",newline="",encoding="utf_8_sig") as csvFile:  # 開啟CSV樣本
        fields = ["編號","公司名稱","職務名稱"]
        dictWriter = csv.DictWriter(csvFile,fieldnames = fields)  # 建立物件
        dictWriter.writeheader()  # 欄位名稱
        for row in company_job:
            dictWriter.writerow(row)

def main():    
    urls = ['https://www.104.com.tw/jobs/search/?keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=2&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=4&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=5&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
        ]
            
    
    m = 1
    for url in urls:
        print('-'*50)
        print('...page.'+str(m))
        print('-'*50)
        job_list(url)
        time.sleep(random.randint(3,6))
        m+=1
    write_to_csv()
    
n = 1
company_job=[]
main()

