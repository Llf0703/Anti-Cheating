import yaml
import urllib.request


def get_yaml():
    f = open('config.yaml', 'r', encoding='utf-8')
    config = yaml.load(f.read())
    return config


config = get_yaml()


def get_html(url):
    headers = (
        'User-Agent', config['ua'])
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    try:
        page = opener.open(url, timeout=config['time_out'])
    except Exception as e:
        print('错误：'+str(e)+' ，已跳过，请检查网络连接或修改最长等待时间')
        return ''
    try:
        html = page.read()
    except Exception as e:
        print('错误：'+str(e)+' ，已跳过，请检查网络连接或修改最长等待时间')
        return ''
    html = html.decode("utf8", "ignore")
    return html
