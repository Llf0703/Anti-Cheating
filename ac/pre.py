import urllib.request
import yaml

def get_yaml():
    f = open('config.yaml', 'r', encoding='utf-8')
    config = yaml.load(f.read())
    return config

def get_html(url):
    headers = ('User-Agent', get_yaml()['user_agent'])
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    page = opener.open(url)
    html = page.read()
    html = html.decode("utf8","ignore")
    return html