# 下载选手代码

from ac.pre import get_yaml
from ac.pre import get_html
from urllib.request import quote
import re
import os

config = get_yaml()

contest_url = str(config['oj_url'])+'/contest/'+str(config['contest_id'])

def user():
    overview_url = contest_url+'/standings'
    overview = get_html_withjs(overview_url)
    overview_reg = re.compile(r'<a href=\"(.+?)\" class=\"uoj-score\"')
    all_submissions = overview_reg.findall(overview)

    print(overview)

    for i in all_submissions:
        print(i)
        sub_url = config['oj_url']+i
        sub = get_html(sub_url)
        get_problem_id = re.compile(r'#(\d).')
        problem_id = re.search('#(\d).',sub)
        print(problem_id)

user()