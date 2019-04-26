# Anti-Cheating OI全网反作弊系统

![](https://img.shields.io/badge/python-3.x-blue.svg?style=flat-square) ![](https://img.shields.io/badge/ubuntu->=16.04-orange.svg?style=flat-square)
![](https://img.shields.io/badge/LICENSE-MIT-green.svg?style=flat-square)

## 使用说明

### 关于模式

- ``v1``是对单独的文件进行反作弊
- ``v2``是对OJ中的比赛进行反作弊（暂时只支持UOJ）

### 准备

目前只在64位的``Ubuntu19.04``,``Ubuntu18.10``,``Ubuntu16.04LTS``,``Ubuntu18.04LTS``,``Windows10``下``Python3.x``环境测试，理论上支持所有现代系统。

需要提前安装[SIM](https://dickgrune.com/Programs/similarity_tester/)，可以下载编译或直接使用命令安装：

```
sudo apt-get install similarity-tester
```

项目依赖``PyYAML``，如果需要使用``v2``模式，还需要安装``Senlenium``，在终端执行：

```
sudo pip install -r requirements.txt
```

``Senlenium``默认使用``GeckoDriver``，请到 [mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases) 下载

### 设置

打开``config.yaml``按照说明进行设置。

### 运行

```
python3 main.py
```

## Features

### v1.0

1. 代码匹配率高
2. ~~支持多种搜索引擎~~（因为必应没什么卵用所以我把它去了）

### v2.0

1. 支持UOJ一键操作，也同样保留了原版功能
2. 设置项更加丰富
3. 修复了遇到404页面时报错退出的bug
4. 修复了爬取``cnblogs.com``行号删除不完全的bug

## TODO

- [ ] 更多搜索引擎(Bing,Google)的支持
- [ ] 按相似度排序
- [ ] 命令行传参支持

## LICENSE

MIT

## 相关项目

[Duanyll/VJudge-Anti-Cheating](https://github.com/Duanyll/VJudge-Anti-Cheating) :  基于SIM的vjudge比赛反抄袭工具，使用C#编写。