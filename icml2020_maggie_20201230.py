# -*- coding: utf-8 -*-
"""
Created on Dec 30  2020
Download  ICML2020 Proceeding
@author: maggie
"""

from bs4 import BeautifulSoup 
import re
import urllib.request
import json
import time

def DownloadPaper(paper_dic_i):
    paper_url = "http://proceedings.mlr.press/v119/"+str(paper_dic_i[1])+"/"+str(paper_dic_i[1])+".pdf"
    print(paper_dic_i[0])
    print("downloading paper: ")
    paper_req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    paper_req= urllib.request.Request(url=paper_url, headers = paper_req_headers)
    print("point A")
    
    try:
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容
    except:
        time.sleep( 10 )
        paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
        paper_res_data=paper_res.read()#获取res响应体中的内容       

    papername = paper_dic_i[0].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_").replace(":","").replace('"','').replace("$","").replace("\\","_").replace("*","")
    with open('C:\\Users\\maggie\\.spyder-py3\\ICML2020\\'+papername+".pdf","wb") as code:
            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete.")
    
url="http://proceedings.mlr.press/v119/"

"""
print ("method 1:")
response1=urllib.request.urlopen(url,)
print ("获取状态码，200表示成功:")
print (response1.getcode())
"""

    
req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
res=urllib.request.urlopen(req)#发送请求对象req
res_data=res.read().decode('utf-8')#获取res响应体中的内容
#print(res_data)

html=BeautifulSoup(res_data,'html.parser')
html_body=html.body
#print(html_body)

div=html.select('.paper')
#print(div)
div_str = str(div)
#print(div_str)

paper_dic_title=re.findall('<p.*?class="title">(.*?)</p>',div_str,re.S)
#print(len(paper_dic_title))
#print(paper_dic_title)

paper_dic_link=re.findall('<p class="links">\s*\[<a.*?href="http://proceedings.mlr.press/v119/(.*?)\.html">abs</a>',div_str,re.S)
#print(len(paper_dic_link))
#print(paper_dic_link)

paper_dic=list(zip(paper_dic_title,paper_dic_link))
#print(paper_dic)

for i in range(1,1085):
    print("第"+str(i)+"篇")
    DownloadPaper(paper_dic[i-1])
   

    

