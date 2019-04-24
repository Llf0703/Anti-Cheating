import urllib.request
import yaml

def get_yaml():
    f = open('config.yaml', 'r', encoding='utf-8')
    config = yaml.load(f.read())
    return config

def get_html(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try: page = opener.open(url)
    except urllib.error.HTTPError as e:
        print('错误：'+str(e))
        return ''
    else:
        html = page.read()
        html = html.decode("utf8","ignore")
        return html