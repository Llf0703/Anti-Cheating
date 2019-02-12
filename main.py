from ac.pre import get_yaml
from ac.baidu import baidu

config = get_yaml()

print('搜索关键字：'+config['keyword']+'\n搜索页数：'+str(config['baidu_pages'])+'\n输出大于'+str(config['sim_limit'])+'%的结果\n使用搜索引擎：'+config['site']+'\n---------------\n')

if config['site']=='baidu':
    baidu(config)