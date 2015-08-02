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

        (3) git clone osmo项目

        (4) 进入osmo目录

        (5) 编译
            $ python setup.py build

        (6) 安装
            $ python setup.py install

        (7) 输入python
            (test)➜  ~  python
            Python 2.7.5 (default, Mar  9 2014, 22:15:05)
            [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
            Type "help", "copyright", "credits" or "license" for more information.
            >>> import osmo
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
