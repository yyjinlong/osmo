osmo
====

## pypi地址

```
https://pypi.python.org/pypi/osmo
```

## 安装

```
pip install osmo
```

## 引用说明

OpenStack的通用库 (oslo) 包含了众多不需要重复发明的"轮子"。

  * oslo.config 库用于解析命令行和配置文件中的配置选项。

  * oslo.db 是针对SQLAlchemy的访问抽象。

  * oslo.log(logging) 为OpenStack项目提供了标准的logging配置。


## 目标

应用服务公共库:

  * 简化damon应用的创建, 并返回对应的entry_point。

  * 对oslo.db的使用进行封装，已达到拿来即用的目的。

  * 对flask进行创建和初始化。

  * 使用flask框架创建wsgi应用，并基于blueprint创建web应用。

  * 对gunicorn进行封装，填充默认参数，如worker数量、access log、timeout等。

  * 通过与oslo.config结合，使其在启动时可动态选择wsgi server，默认为werkzeug。线上运行则使用—run_mode=gunicorn 来运行wsgi应用。
