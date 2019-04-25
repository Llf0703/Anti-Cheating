from ac.user import user
from ac.pre import get_yaml
from ac.compare import compare
from ac.download import download

if __name__ == '__main__':
    config = get_yaml()
    print('比赛编号：'+str(config['contest_id'])+'\n搜索页数：'+str(config['pages'])+'页\n相似度阀值：'+str(
        config['sim_limit'])+'%\n最多等待：'+str(config['time_out'])+'s\n----------------------------------------')
    download()
    user()
    compare()
    print('完成！请打开result.txt查看结果')
