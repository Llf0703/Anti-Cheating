import urllib.request
import re
import time
import os
import yaml
from urllib.request import quote


def get_html(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    page = opener.open(url)
    html = page.read()
    html = html.decode("utf8","ignore")
    return html

def get_yaml():
    f = open('config.yaml', 'r', encoding='utf-8')
    config = yaml.load(f.read())
    return config

config = get_yaml()

page_cnt = 0

kw=quote(config['keyword'])

print('搜索关键字：'+config['keyword']+'\n搜索页数：'+str(config['baidu_pages'])+'\n输出大于'+str(config['sim_limit'])+'%的结果\n---------------\n')

baidu_url = 'https://www.baidu.com/s?wd='+kw

cnt=0

result=open('result.txt','w')

while page_cnt<config['baidu_pages']:
    reglist=[]
    page_cnt=page_cnt+1
    print('正在搜索第 '+str(page_cnt)+' 页')
    html = get_html(baidu_url)
    reg = r'<div class=\"f13\"><a target=\"_blank\" href=\"(.+?)\" class=\"c-showurl\" style=\"text-decoration:none;\">'
    c_reg = re.compile(reg)
    reglist += c_reg.findall(html)

    codelist = []

    for i in reglist:
        url=i
        html=get_html(url)
        line_id=re.compile(r'<span style=\"color: #008080\">(.+?)</span>',re.S) #cnblogs行号
        html=line_id.sub('',html)
        code=r'#include([\s\S]*?)</pre>'
        c_code=re.compile(code)
        codelist=c_code.findall(html)
        cnt=cnt+1
        now=str(cnt)
        file=open('b.cpp','w')
        for j in codelist:
            pattern = re.compile(r'<[^>]+>', re.S)
            j = pattern.sub('', j)
            j='#include'+j
            j=j.replace("&lt;","<")
            j=j.replace("&gt;",">")
            j=j.replace("&amp;","&")
            j=j.replace("&quot;",'"')
            file.write(j)
        file.close()
        os.system('sim_c++ -p -o re.txt a.cpp b.cpp')
        f=open('re.txt')
        data=f.read()
        a=re.compile(r'a.cpp consists for(.+?)% of b.cpp material')
        datalist=a.findall(data)
        f.close()
        for k in datalist:
            ans=int(k)
            if ans>=config['sim_limit']:
                result.write(url+'\n相似度：'+str(ans)+'%'+'\n\n')
    
    baidu_url='https://www.baidu.com/s?wd='+kw+'&pn='+str(page_cnt)+'0'

result.close()

print('完成！请打开result.txt查看结果。')