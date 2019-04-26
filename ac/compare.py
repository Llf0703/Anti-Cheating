# 对比下载代码与选手提交代码

import os
import re
import shutil
from ac.pre import get_yaml

config = get_yaml()


def compare():
    print('\n正在进行比较，即将得到结果...')

    file = open('result.txt', 'w')

    data_dir = 'data'
    user_dir = 'user'

    cpp = re.compile(r'.cpp')

    user_list = os.listdir(user_dir)
    for i in range(0, len(user_list)):
        user_problem_dir = os.path.join(user_dir, user_list[i])
        problem_id = os.path.basename(user_problem_dir)

        user_code_list = os.listdir(user_problem_dir)
        for j in range(0, len(user_code_list)):
            user_code_dir = os.path.join(user_problem_dir, user_code_list[j])
            user_name = os.path.basename(user_code_dir)
            user_name = cpp.sub('', user_name)

            data_list = os.listdir(data_dir)
            for k in range(0, len(data_list)):
                data_problem_dir = os.path.join(data_dir, data_list[k])
                if os.path.basename(data_problem_dir) != problem_id:
                    continue

                data_code_list = os.listdir(data_problem_dir)
                for l in range(0, len(data_code_list)):
                    data_code_dir = os.path.join(
                        data_problem_dir, data_code_list[l])

                    f = open(data_code_dir)
                    code = f.read()
                    f.close()
                    data_name = re.search('url:(.+?):end', code).group(1)

                    os.system('sim_c++ -p -o re.txt ' +
                              user_code_dir+' '+data_code_dir)
                    f = open('re.txt')
                    res = f.read()
                    f.close()
                    result = re.search('consists for(.+?)% of', res)
                    if result == None:
                        continue
                    result = int(result.group(1))
                    if result >= config['sim_limit']:
                        file.write(user_name+' 在 #'+str(problem_id)+' 提交的代码与 ' +
                                   data_name+' 相似度为 '+str(result)+'%\n')

    file.close()
    os.remove('re.txt')
    shutil.rmtree('data')
    shutil.rmtree('user')
    return
