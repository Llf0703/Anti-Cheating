#得到比赛题号与序号关联的信息方便爬取时确定是哪一道题

from urllib.request import quote
import re
from ac.pre import get_html

def contest_info(config):
