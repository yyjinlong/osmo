osmo
====
[![](https://api.travis-ci.org/yyjinlong/osmo.png?branch=master)](https://travis-ci.org/yyjinlong/osmo)

## pypi地址

```
https://pypi.python.org/pypi/osmo
```

## 安装

```
pip install osmo
```


## 引用说明

> OpenStack的通用库 (`oslo`) 包含了众多不需要重复发明的"轮子"。
>* `oslo.config` 库用于解析命令行和配置文件中的配置选项。
>* `oslo.db` 是针对 `SQLAlchemy` 的访问抽象。
>* `oslo.log`( `logging` ) 为OpenStack项目提供了标准的`logging`配置。


## 目标

`osmo`作为一个应用服务公共库，主要满足如下目标:

* 简化`damon`应用的创建, 并返回对应的`entry_point`。

* 对`oslo.db`的使用进行封装，已达到拿来即用的目的。

* 对`flask`进行创建和初始化。

* 使用`flask`框架创建`wsgi`应用，并基于`blueprint`创建`web`应用。

* 对`gunicorn`进行封装，填充默认参数，如`worker数量、access log、timeout`等。

* 通过与`oslo.config`结合，使其在启动时可动态选择`wsgi server`，默认为`werkzeug`。线上运行则使用`—run_mode=gunicorn` 来运行wsgi应用。
