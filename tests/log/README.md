# openstack log module

    log目录下的文件都是从opentstack拿过来的，需要学习。


# log install

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


# log test

    test.conf 测试log的配置文件
    test.py   测试log的运行文件

    注：
    log.py文件里用到了CONF模块，所以必须得在调用log模块前使oslo.conf生效

    所以，应用启动前，需要添加如下conf配置：
    cfg.CONF(sys.argv[1:], project='test', version='1.0',default_config_files=None)
