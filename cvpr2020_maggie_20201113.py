# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:22:43 2020
Download CVPR2020 Proceeding
@author: maggie
"""

from bs4 import BeautifulSoup 
import urllib.request
import re

def DownloadPaper(paper_id):
    paper_url = "http://openaccess.thecvf.com/content_CVPR_2020/papers/"+paper_id
    print("downloading paper: ")
    #papername = paper['title'].replace(" ","_").replace(":","").replace("?","").replace("/","_").replace("|","_")
    paper_req= urllib.request.Request(url=paper_url, headers = req_headers)
    paper_res=urllib.request.urlopen(paper_req)#发送请求对象req
    paper_res_data=paper_res.read()#获取res响应体中的内容
    #print(res2_data)
    with open('C:\\Users\\maggie\\.spyder-py3\\CVPR2020\\'+paper_id,"wb") as code:
        code.write(paper_res_data)
    print("Complete."+str(paper_id))

    
day=['16','17','18']   
for i in range(len(day)):
    url="https://openaccess.thecvf.com/CVPR2020?day=2020-06-"+str(day[i])
    #url="https://openaccess.thecvf.com/CVPR2020?day=2020-06-16"
    #url="https://openaccess.thecvf.com/CVPR2020?day=2020-06-17"
    #url="https://openaccess.thecvf.com/CVPR2020?day=2020-06-18"
    
    #定义请求头信息，通常只定义 User-Agent
    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

    req=urllib.request.Request(url=url,headers=req_headers)#构造请求对象req
    res=urllib.request.urlopen(req)#发送请求对象req
    res_data=res.read().decode('utf-8')#获取res响应体中的内容
    #print(res_data)
    
    #用BeautifulSoup解析数据 python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
    html=BeautifulSoup(res_data,'html.parser')
    a=html.select('a')
    a_str = str(a)
    paper_dic=re.findall('<a.*?href="content_CVPR_2020/papers/(.*?)">pdf</a>',a_str,re.S)
    
    for paper_id in paper_dic:
        DownloadPaper(paper_id) #paper_id='Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf'






























