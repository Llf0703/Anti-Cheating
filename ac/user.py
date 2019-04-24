# 下载选手代码

# finished

from ac.pre import get_yaml
from ac.pre import get_html
from urllib.request import quote
from selenium import webdriver
import re
import os

config = get_yaml()

contest_url = str(config['oj_url'])+'/contest/'+str(config['contest_id'])

driver = webdriver.Firefox() 

def user():
    overview_url = contest_url+'/standings'
    driver.get(overview_url)
    overview = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    overview_reg = re.compile(r'<td><div><a href=\"/submission/([0-9]{1,})\" class=\"uoj-score\" style=\"color\:rgb\(0,204,0\)\">100</a></div>')
    all_submissions = overview_reg.findall(overview)
    driver.close()

    if not os.path.exists('user'):
        os.makedirs('user')

    for i in all_submissions:
        # get info
        sub_url = config['oj_url']+'/submission/'+str(i)
        sub = get_html(sub_url)
        name = re.search('<span class=\"uoj-username\" data-rating=\"([0-9]{1,})\">(.+?)</span>',sub).group(2)
        problem_id = re.search('<a href=\"/contest/(.+?)\">#([0-9]{1,})\.(.+?)</a>',sub).group(2)
        code = re.search('#include([\s\S]*?)</pre>',sub).group(1)
        pattern = re.compile(r'<[^>]+>', re.S)
        code = pattern.sub('', code)
        code = '#include'+code
        code = code.replace("&lt;","<")
        code = code.replace("&gt;",">")
        code = code.replace("&amp;","&")
        code=code.replace("&quot;",'"')

        # write in local
        if not os.path.exists('user/'+str(problem_id)):
            os.makedirs('user/'+str(problem_id))
        file = open('user/'+str(problem_id)+'/'+str(name)+'.cpp','w')
        file.write(code)
        file.close()