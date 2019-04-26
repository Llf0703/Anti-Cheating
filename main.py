from ac.pre import get_yaml
from ac.compare import compare
from v1.baidu import baidu
from v2.user import user
from v2.download import download


def v1():
    print('搜索关键字：'+config['keyword']+'\n搜索页数：'+str(config['pages'])+'\n输出大于'+str(
        config['sim_limit'])+'%的结果\n使用搜索引擎：'+config['site']+'\n---------------\n')
    if config['site'] == 'baidu':
        baidu(config)


def v2():
    print('比赛编号：'+str(config['contest_id'])+'\n搜索页数：'+str(config['pages'])+'页\n使用搜索引擎'+config['site']+'\n相似度阀值：'+str(
        config['sim_limit'])+'%\n最多等待：'+str(config['time_out'])+'s\n----------------------------------------')
    download()
    user()
    compare()
    print('完成！请打开result.txt查看结果')


if __name__ == '__main__':
    config = get_yaml()
    if config['mode'] == 1:
        v1()
    elif config['mode'] == 2:
        v2()
    else:
        print('模式不合法！')
