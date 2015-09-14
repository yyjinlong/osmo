osmo(openstack module) - keeping moving!
----------------------------------------

## 俗话说得好：好记性不如烂笔头

## 使用方法一：

    1) 安装virtualenv
        $ virtualenv test

    2) 激活virtualenv
        $ source test/bin/activate

    3) git clone osmo项目

    4) 进入osmo目录

    5) 编译
       $ python setup.py build

    6) 安装
       $ python setup.py install

    7) 查看
        (test)➜  ls .venv/lib/python2.7/site-packages/osmo*
        app  core  db  __init__.py  __init__.pyc  web

        .venv/lib/python2.7/site-packages/osmo-0.0.1.dev2-py2.7.egg-info:
        dependency_links.txt  not-zip-safe  pbr.json  PKG-INFO  requires.txt  SOURCES.txt  top_level.txt

    8) 输入python
        (test)➜  ~  python
        Python 2.7.5 (default, Mar  9 2014, 22:15:05)
        [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import osmo
        >>>

## 使用方法二：

    1) 安装virtualenv
        $ virtualenv .venv

    2) 激活virtualenv
        $ source .venv/bin/activate

    3) 添加requirements.txt
	git+git://github.com/yyjinlong/osmo.git#egg=osmo

    4) pip安装
        (.venv)➜  test  pip install -r requirements.txt

    5) 错误
	Error: pg_config executable not found.

    6) 解决
	➜  ~ sudo apt-get install libpq-dev python-dev
	之后再重新执行一遍就搞定

## 使用方法三：

    本地搭建pypi服务器,使用pip再下载.

## 注：

    requirement.txt里必须指定版本号.
