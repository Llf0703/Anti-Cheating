# Anti-Cheating OI全网反作弊系统

![](https://img.shields.io/badge/python-3.6.7-blue.svg) ![](https://img.shields.io/badge/ubuntu-18.10-orange.svg)
![](https://img.shields.io/badge/LICENSE-MIT-green.svg)

## 使用说明

**暂时只支持C++语言**

需要提前安装[SIM](https://dickgrune.com/Programs/similarity_tester/)，可以下载编译或直接使用命令安装：

```
sudo apt-get install similarity-tester
```

将需要比对的代码放入``a.cpp``，然后运行``ac.py``，输入当前题目的关键字即可。

eg:
题目：[Mayan游戏](https://www.luogu.org/problemnew/show/P1312)

```
python3 ac.py
请输入搜索关键字：Mayan puzzle是最近流行起来的一个游戏。游戏界面是一个7 行×5 
```

程序会自动生成``b.cpp``,``re.txt``,``result.txt``，其中前两个是没用的，删掉或不删皆可，结果在``result.txt``中，会给出网址和相似度，如：

```
http://www.baidu.com/link?url=xxxxx
相似度：100%
```

然后手工比对即可。

## 高级设置

### 百度搜索页数

在``ac.py:27``

```py
while page_cnt<3:
```

把3改成你想要搜索的页数即可，一般样本越多效果越好，但时间耗费较多。

### 相似度阀值

在``ac.py:66``

```py
if ans>=10:
```

将10改成想要的阀值即可。相似度超过阀值就会输出到``result.txt``中。

## Feature

1. 100%的代码匹配率（经过本人测试过3道题后得出的结论）
2. 使用方便，只需安装python即可

## TODO

- [ ] 按相似度排序
- [ ] 人性化的设置界面
- [ ] 更多语言支持

## LICENSE

MIT

## 相关项目

[Duanyll/VJudge-Anti-Cheating](https://github.com/Duanyll/VJudge-Anti-Cheating) :  基于SIM的vjudge比赛反抄袭工具，使用C#编写。