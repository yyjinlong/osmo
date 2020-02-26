osmo库的测试用例
----------------

## 开发测试

    1 创建虚拟环境

        ➜  cd osmo
        ➜  osmo git:(master) ✗ virtualenv3 .venv
        ➜  osmo git:(master) ✗ source .venv/bin/activate

    2 打包osmo

        (.venv) ➜  osmo git:(master) ✗ pip install -r requirements.txt
        (.venv) ➜  osmo git:(master) ✗ python setup.py develop

        说明: develop模式会在site-packages下生成osmo.egg-link
        (.venv) ➜  osmo git:(master) ✗ ls .venv/lib/python3.6/site-packages/osmo.egg-link
        .venv/lib/python3.6/site-packages/osmo.egg-link

    3 开发测试

        (.venv) ➜  osmo git:(master) ✗ cd tests
        (.venv) ➜  tests git:(master) ✗ ls

        (.venv) ➜  tests git:(master) ✗ pip install -r requirements.txt


    4 base模块

        (.venv) ➜  tests git:(master) ✗ python test_base.py --config-file=test.conf


    5 db模块

        1 创建数据库

            create table users(
                id serial, 
                name varchar(100), 
                primary key(id)
            );

        2 插入数据

            insert into users (name) values('zhangsan');
            insert into users (name) values('lisi');
            insert into users (name) values('wangwu');

        3 运行

            (.venv) ➜  tests git:(master) ✗ python test_db.py --config-file=test.conf


    6 wsgi模块

        (.venv) ➜  tests git:(master) ✗ cd web
        (.venv) ➜  web git:(master) ✗ python test_wsgi.py --config-file=test.conf
