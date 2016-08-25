# oslo.db

    models目录：
        base.py     -- common function file
        users.py    -- model file

    services目录:
        test.py     -- database curd service file

# study

    db/api.py:
        get_session function:
            See: http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html
                 UnitofWork-contextual(上下文作业单元)

# install

    1) 安装pg库、sqlalchemy、oslo.db

        (.venv) ➜  db git:(master) ✗ pip install -r requirements.txt

    2) 创建test数据库及users表
        ➜  ~ psql -U postgres -d postgres
        postgres=# create database test;
        CREATE DATABASE
        lopez=# \c test
        You are now connected to database "test" as user "postgres".
        test=#
        test=# create table users (                                                                                                                                                       id serial primary key,                                                                                                                                                            name varchar(20));
        CREATE TABLE
        test=#
        test=# insert into users (name) values ('yangjinlong');
        INSERT 0 1
        test=#

    2) 运行

        (.venv) ➜  db git:(master) ✗ python test.py --config-file=test.conf
        .....result:  [u'yangjinlong']
