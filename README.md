# Anti-Cheating OI全网反作弊系统

![](https://img.shields.io/badge/python-3.x-blue.svg?style=flat-square) ![](https://img.shields.io/badge/ubuntu->=16.04-orange.svg?style=flat-square)
![](https://img.shields.io/badge/LICENSE-MIT-green.svg?style=flat-square)

## 使用说明

### 准备

**暂时只支持C和C++语言**

目前只在64位的``Ubuntu18.10``,``Ubuntu16.04LTS``,``Ubuntu18.04LTS``,``Windows10``下``Python3.x``环境测试，理论上支持所有现代系统。

需要提前安装[SIM](https://dickgrune.com/Programs/similarity_tester/)，可以下载编译或直接使用命令安装：

```
sudo apt-get install similarity-tester
```

项目依赖``PyYAML``，在终端执行以下代码：

```
sudo pip install pyyaml
```

### 设置

**搜索引擎暂时只支持百度和必应**

设置项在``config.yaml``，以下是以[Mayan游戏](https://www.luogu.org/problemnew/show/P1312)为例的默认设置：

```yaml
# 搜索关键字，建议粘贴题目中的一段文字或准确题号
keyword: Mayan puzzle是最近流行起来的一个游戏。游戏界面是一个7行×5

# 搜索页数，越多越精确，但耗时更多
pages: 3

# 相似度阀值，即相似度超过这个百分比就会输出到result.txt中
sim_limit: 10

# 使用搜索引擎设置，百度为baidu，必应为bing，谷歌为google(谷歌暂不支持)
site: baidu

# 浏览器useragent，若没有特殊情况可以保持默认
user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
```

按照提示修改设置项后保存即可。

### 运行

将需要比对的代码放入``a.cpp``，然后运行``main.py``。

```
python3 main.py
```

程序会自动生成``b.cpp``,``re.txt``,``result.txt``，其中前两个是没用的，删掉或不删皆可，结果在``result.txt``中，会给出网址和相似度，如：

```
https://www.example.com
相似度：100%
```

然后手工比对即可。

## Feature

1. 100%的代码匹配率（经过本人测试过10多道题后得出的结论）
2. 使用方便，只需安装python即可

## TODO

- [x] 人性化的设置界面
- [ ] 更多搜索引擎(Bing,Google)的支持
- [ ] 按相似度排序
- [ ] (Duanyll大佬建议) 命令行传参支持
- [ ] 对Pascal语言的支持

## LICENSE

MIT

## 相关项目

[Duanyll/VJudge-Anti-Cheating](https://github.com/Duanyll/VJudge-Anti-Cheating) :  基于SIM的vjudge比赛反抄袭工具，使用C#编写。