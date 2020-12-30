# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:29:59 2020
Download  ICLR2020 Proceeding
@author: maggie
"""

import urllib.request
import json




def DownloadPaper(paper_dic_i):
    paper_url = "https://openreview.net/pdf?id="+paper_dic_i["id"]
    print("downloading paper: ")
    #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    paper_req= urllib.request.Request(url=paper_url, headers = req_headers)
    paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
    paper_res_data=paper_res.read()#获取res响应体中的内容
    #print(res2_data)
#   with open('C:\\Users\\maggie\\.spyder-py3\\CVPR2020\\'+paper_id,"wb") as code:
    papername = paper_dic_i["content"]["title"].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_").replace(":","").replace('"','').replace("$","").replace("\\","_")
    with open('C:\\Users\\maggie\\.spyder-py3\\ICLR2020\\'+papername+".pdf","wb") as code:
            code.write(paper_res_data)
            #urllib.request.urlretrieve(url, papername+".pdf")
    print("Complete."+str(papername))
    
url="https://iclr.cc/virtual_2020/papers.json"

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

paper_dic=json.loads(res_data)
#print(paper_dic)
for i in range(686):
    DownloadPaper(paper_dic[i])

    

