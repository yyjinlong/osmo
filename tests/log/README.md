# openstack log module

    log目录下的文件都是从opentstack拿过来的，需要学习。


# log install

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


# log test

    test.conf 测试log的配置文件
    test.py   测试log的运行文件

    注：
    log.py文件里用到了CONF模块，所以必须得在调用log模块前使oslo.config生效

    所以，应用启动前，需要添加如下conf配置：
    cfg.CONF(sys.argv[1:], project='test', version='1.0',default_config_files=None)

    运行:
    (.venv) ➜  log git:(master) ✗ python test.py --config-file=test.conf
