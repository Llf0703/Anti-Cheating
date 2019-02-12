from urllib.request import quote
import re
import os
from ac.pre import get_html

def bing(config):
    page_cnt = 0

    kw=quote(config['keyword'])

    bing_url = 'https://cn.bing.com/search?q='+kw+'&go=%e6%90%9c%e7%b4%a2&qs=ds&FORM=PORE'

    cnt=0

    result=open('result.txt','w')

    while page_cnt<config['pages']:
        reglist = []
        print(bing_url)
        page_cnt=page_cnt+1
        print('正在搜索第 '+str(page_cnt)+' 页')
        html = get_html(bing_url)
        result.write(html)
        reg = r'<h2><a target=\"_blank\" href=\"(.+?)\"'
        c_reg = re.compile(reg)
        reglist += c_reg.findall(html)

        codelist = []

        for i in reglist:
            url=i
            print(url)
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
                    
        bing_url='https://cn.bing.com/search?q='+kw+'&go=%e6%90%9c%e7%b4%a2&qs=ds&first='+str(page_cnt)+'1&FORM=PORE'

    result.close()

    print('完成！请打开result.txt查看结果。')
    return