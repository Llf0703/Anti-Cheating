# 下载选手代码

import re
import os
from ac.pre import get_yaml
from ac.pre import get_html
from selenium import webdriver
from urllib.request import quote
from selenium.webdriver.firefox.options import Options

config = get_yaml()

contest_url = str(config['oj_url'])+'/contest/'+str(config['contest_id'])

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)


def user_uoj():
    print('\n正在从OJ获取选手提交代码...\n----------------------------------------')

    overview_url = contest_url+'/standings'
    driver.get(overview_url)
    overview = driver.execute_script(
        "return document.getElementsByTagName('html')[0].innerHTML")
    overview_reg = re.compile(
        r'<td><div><a href=\"/submission/([0-9]{1,})\" class=\"uoj-score\" style=\"color\:rgb\(0,204,0\)\">100</a></div>')
    all_submissions = overview_reg.findall(overview)
    driver.quit()

    if not os.path.exists('user'):
        os.makedirs('user')

    for i in all_submissions:
        print('正在查询 #'+str(i)+' 提交记录...')
        sub_url = config['oj_url']+'/submission/'+str(i)
        sub = get_html(sub_url)
        name = re.search(
            '<span class=\"uoj-username\" data-rating=\"([0-9]{1,})\">(.+?)</span>', sub).group(2)
        problem_id = re.search(
            '<a href=\"/contest/(.+?)\">#([0-9]{1,})\.(.+?)</a>', sub).group(2)
        code = re.search(
            '<code class=\"(.+?)\">([\s\S]*?)</code>', sub).group(2)
        code = code.replace("&lt;", "<")
        code = code.replace("&gt;", ">")
        code = code.replace("&amp;", "&")
        code = code.replace("&quot;", '"')

        if not os.path.exists('user/'+str(problem_id)):
            os.makedirs('user/'+str(problem_id))
        file = open('user/'+str(problem_id)+'/'+str(name)+'.cpp', 'w')
        file.write(code)
        file.close()

    return


def user():
    user_uoj()
    return
