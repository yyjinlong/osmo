## flask

    主要文件说明：

        singleton.py   : 定义的一个单实例类

        application.py : 一个应用类，主要是QApplication,一些入口点都继承它

        wsgiapp.py     : 对flask的初始化及运行适配.
                         注：(调试：werzeug；线上：gunicorn)


## 测试文件

    static:     静态文件目录, 存放css、javascript文件
    templates:  模板文件目录, 存放html模板文件
    views:      存放蓝图文件

    zero.py:    继承WsgiApplication并定义应用名name和版本version
    注: 对于web项目,只需要重载父类的init_flask_app这个方法即可.
        在这个方法里初始化flask一些相关属性及注册蓝图.


## 测试

    1) 依赖
        requirements.txt：
            flask == 0.10.1
            gunicorn == 19.3.0
            gevent == 1.1.1

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

        安装依赖
        (.venv) ➜  web git:(master) ✗ pip install -r requirements.txt

        调试启动服务:
        (.venv) ➜  web git:(master) ✗ python zero.py --config-file=zero.conf

        gunicorn启动:
        (.venv) ➜  web git:(master) ✗ python zero.py --web-run_mode=gunicorn --config-file=zero.conf

        测试接口:
        (.venv) ➜  web git:(master) ✗ curl -H 'Content-Type:application/json' -d '{"name":"jinlong.yang"}' localhost:4000/test

        测试界面:
        浏览器输入：http://0.0.0.0:4000/
