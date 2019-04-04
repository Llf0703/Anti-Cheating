# 下载选手代码

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

    for i in all_submissions:
        sub_url = config['oj_url']+'/submission/'+str(i)
        sub = get_html(sub_url)

user()