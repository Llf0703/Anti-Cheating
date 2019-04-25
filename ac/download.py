# 下载百度搜索代码

import re
import os
from ac.pre import get_yaml
from ac.pre import get_html
from urllib.request import quote

config = get_yaml()


def download():

    print('\n正在从搜索引擎获取比对代码...\n----------------------------------------')

    word_cnt = -1
    if not os.path.exists('data'):
        os.makedirs('data')

    for word in config['keywords']:

        page_cnt = 0
        word_cnt = word_cnt + 1
        if not os.path.exists('data/'+str(config['problems'][word_cnt])):
            os.makedirs('data/'+str(config['problems'][word_cnt]))
        kw = quote(word)
        baidu_url = 'https://www.baidu.com/s?wd='+kw
        cnt = 0
        print('开始搜索第 '+str(word_cnt+1)+' 题，搜索关键字：'+word +
              '，共 '+str(len(config['keywords']))+' 题...')

        while page_cnt < config['pages']:
            reglist = []
            page_cnt = page_cnt+1
            print('正在搜索第 '+str(page_cnt)+' 页，共 '+str(config['pages'])+' 页...')
            html = get_html(baidu_url)
            reg = r'<div class=\"f13\"><a target=\"_blank\" href=\"(.+?)\" class=\"c-showurl\" style=\"text-decoration:none;\">'
            c_reg = re.compile(reg)
            reglist += c_reg.findall(html)

            codelist = []

            for i in reglist:
                url = i
                html = get_html(url)
                print(url)
                line_id = re.compile(
                    r'<span style=\"color: #008080\">(.+?)</span>', re.S)  # cnblogs行号
                html = line_id.sub('', html)
                code = r'#include([\s\S]*?)</pre>'
                c_code = re.compile(code)
                codelist = c_code.findall(html)
                cnt = cnt+1
                file = open(
                    'data/'+str(config['problems'][word_cnt])+'/'+str(cnt)+'.cpp', 'w')
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

            baidu_url = 'https://www.baidu.com/s?wd=' + \
                kw+'&pn='+str(page_cnt)+'0'

    return
