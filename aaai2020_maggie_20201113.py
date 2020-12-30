# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:28:33 2020
Download  AAAI2020 Proceeding
@author: maggie
"""
"""
AAAI论文太多了 我只挑了4个涉及adversarial example的tissue下载
No.1
https://aaai.org/ojs/index.php/AAAI/issue/view/249

No.4
https://aaai.org/ojs/index.php/AAAI/issue/view/252

No.7
https://aaai.org/ojs/index.php/AAAI/issue/view/255

No.10
https://aaai.org/ojs/index.php/AAAI/issue/view/258

所有会场在这
https://aaai.org/Library/AAAI/aaai20contents.php
"""
from bs4 import BeautifulSoup 
import urllib.request
import re
import time

def DownloadPaper(paper_dic,folder_name):
    paper_url = "https://aaai.org/ojs/index.php/AAAI/article/view/"+paper_dic[1]
    print("downloading paper: ")
    #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    paper_req= urllib.request.Request(url=paper_url, headers = req_headers)
    try:
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容
    except:
        time.sleep( 10 )
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容       
    
    #print(res2_data)
#   with open('C:\\Users\\maggie\\.spyder-py3\\CVPR2020\\'+paper_id,"wb") as code:
    papername = paper_dic[0].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_").replace(":","").replace('"','').replace("$","").replace("\\","_")
    with open('C:\\Users\\maggie\\.spyder-py3\\AAAI\\No.'+folder_name+'\\'+papername+".pdf","wb") as code:
            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")


def DownloadProceeding(url_i,folder_i): 
    url="https://aaai.org/ojs/index.php/AAAI/issue/view/"+url_i
    response1=urllib.request.urlopen(url,)
    print ("获取状态码，200表示成功:")
    print (response1.getcode())
    
    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
    try:
        res=urllib.request.urlopen(req)#发送请求对象req
        res_data=res.read().decode('utf-8')#获取res响应体中的内容
    except:
        time.sleep( 10 )
        res=urllib.request.urlopen(req)#发送请求对象req
        res_data=res.read().decode('utf-8')#获取res响应体中的内容      
    print("try完毕")
    html=BeautifulSoup(res_data,'html.parser')
    #html_body=html.body
    #print(html_body)
    
    #paper_html=html.select('.obj_article_summary > .title >a')#按class 名称查找
    paper_html=html.select('.obj_article_summary')#按class 名称查找
    #print(paper_html)
    paper_html_str=str(paper_html)
    paper_dic=re.findall('<div.*?>.*?<a.*?>\n\t\t\t(.*?)\n\t\t\t\t\t</a>.*?<a.*?href="https://aaai.org/ojs/index.php/AAAI/article/view/(.*?)">\n\n\t\t\n\tPDF\n\n\t</a>.*?</div>',paper_html_str,re.S)#这个网页中间搞这么多空格 难怪我PDF匹配不上
    #print(paper_dic)
    print(len(paper_dic))
    
    #print(len(paper_dic))
    for i in range(len(paper_dic)):
        DownloadPaper(paper_dic[i],folder_i)
    
    


urls=['249','252','255','258']
folder=['1','4','7','10']

#urls=['255','258']
#folder=['7','10']

for i in range(len(urls)):
    print("https://aaai.org/ojs/index.php/AAAI/issue/view/"+str(urls[i]))
    DownloadProceeding(urls[i],folder[i])
