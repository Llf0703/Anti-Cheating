import re
import os
from ac.pre import get_html
from urllib.request import quote


def baidu(config):
    page_cnt = 0

    kw = quote(config['keyword'])

    baidu_url = 'https://www.baidu.com/s?wd='+kw

    cnt = 0

    result = open('result.txt', 'w')

    while page_cnt < config['pages']:
        reglist = []
        page_cnt = page_cnt+1
        print('正在搜索第 '+str(page_cnt)+' 页')
        html = get_html(baidu_url)
        reg = r'<div class=\"f13\"><a target=\"_blank\" href=\"(.+?)\" class=\"c-showurl\" style=\"text-decoration:none;\">'
        c_reg = re.compile(reg)
        reglist += c_reg.findall(html)

        codelist = []

        for i in reglist:
            url = i
            print(url)
            html = get_html(url)
            line_id = re.compile(
                r'<span style=\"color: #008080\">(.+?)</span>', re.S)  # cnblogs行号
            html = line_id.sub('', html)
            code = r'#include([\s\S]*?)</pre>'
            c_code = re.compile(code)
            codelist = c_code.findall(html)
            cnt = cnt+1
            now = str(cnt)
            file = open('b.cpp', 'w')
            for j in codelist:
                pattern = re.compile(r'<[^>]+>', re.S)
                j = pattern.sub('', j)
                j = '#include'+j
                j = j.replace("&lt;", "<")
                j = j.replace("&gt;", ">")
                j = j.replace("&amp;", "&")
                j = j.replace("&quot;", '"')
                file.write(j)
            file.close()
            os.system('sim_c++ -p -o re.txt '+config['local']+' b.cpp')
            f = open('re.txt')
            data = f.read()
            a = re.compile(r'a.cpp consists for(.+?)% of b.cpp material')
            datalist = a.findall(data)
            f.close()
            for k in datalist:
                ans = int(k)
                if ans >= config['sim_limit']:
                    result.write(url+'\n相似度：'+str(ans)+'%'+'\n\n')

        baidu_url = 'https://www.baidu.com/s?wd='+kw+'&pn='+str(page_cnt)+'0'

    result.close()
    if os.path.exists('re.txt'):
        os.remove('re.txt')
    if os.path.exists('b.cpp'):
        os.remove('b.cpp')

    print('完成！请打开result.txt查看结果。')
    return
