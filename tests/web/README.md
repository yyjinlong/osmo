## flask

    主要文件说明：

        singleton.py   : 定义的一个单实例类

        application.py : 一个应用类，主要是QApplication,一些入口点都继承它

        flaskapp.py    : 对flask的初始化及运行适配.
                         注：(调试：werzeug；线上：gunicorn)

## 测试文件

    falsk简单测试文件：

        testflask.py  : 使用最简单的werzug.servring下的run_simple来运行

    对于封装的singleton、application、flaskapp的测试:

        testapp.py  : 类似与qg的app.py 和 cmd.py
        testctrl.py : 这个主要是controller里的具体某个接口操作


## 测试

    1) 依赖
        requirements.txt：
            flask
            oslo.config

    2) 安装
        (1) 安装virtualenv
            $ virtualenv test

        (2) 激活virtualenv
            $ source test/bin/activate

        (3) git clone zara项目
        
        (4) 进入zara目录

        (5) 编译
            $ python setup.py build

        (6) 安装
            $ python setup.py install

        (7) 查看
            (test)➜  zara git:(master) ✗ ll ../test/lib/python2.7/site-packages/zara*
            ../../../zero/lib/python2.7/site-packages/zara:
            total 8
            -rw-r--r--   1 qitmak000126  staff     0B  7  3 20:31 __init__.py
            -rw-r--r--   1 qitmak000126  staff   156B  7  3 20:40 __init__.pyc
            drwxr-xr-x  10 qitmak000126  staff   340B  7  3 20:40 db
            drwxr-xr-x  16 qitmak000126  staff   544B  7  3 20:40 log
            drwxr-xr-x  10 qitmak000126  staff   340B  7  3 20:40 web

            ../test/lib/python2.7/site-packages/zara-0.0.0-py2.7.egg-info:
            total 56
            -rw-r--r--  1 qitmak000126  staff   522B  7  3 20:40 PKG-INFO
            -rw-r--r--  1 qitmak000126  staff   534B  7  3 20:40 SOURCES.txt
            -rw-r--r--  1 qitmak000126  staff     1B  7  3 20:40 dependency_links.txt
            -rw-r--r--  1 qitmak000126  staff     1B  7  3 20:35 not-zip-safe
            -rw-r--r--  1 qitmak000126  staff    40B  7  3 20:40 pbr.json
            -rw-r--r--  1 qitmak000126  staff    66B  7  3 20:40 requires.txt
            -rw-r--r--  1 qitmak000126  staff     5B  7  3 20:40 top_level.txt

        (8) 输入python
            (test)➜  ~  python
            Python 2.7.5 (default, Mar  9 2014, 22:15:05)
            [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
            Type "help", "copyright", "credits" or "license" for more information.
            >>> import zara
            >>>


    3) 测试

        进入tests目录
        $ cd tests

        启动服务：
        $ python testapp.py --config-file=test.conf
        或:
        $ python testapp.py

        测试接口：
        $ curl -H 'Content-Type:application/json' -d '{"name":"jinlong.yang"}' localhost:5000/test
