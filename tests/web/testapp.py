# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from zara.web.flaskapp import QFlaskApplication


# 对应qg的app.py，对整个应用的设置及初始化
class Test(QFlaskApplication):
    name = "test"
    version = "v1.0"

    def init_app(self):
        super(Test, self).init_app()
        app = self.flask_app
        app.secret_key = "12345"

        # 注册蓝图
        self.setup_blueprint()

    def setup_blueprint(self):
        app = self.flask_app

        import testctrl
        app.register_blueprint(testctrl.bp, url_prefix="")


# 测试 -- 对应qg的cmd.py,给出函数地址的返回值
t = Test()
test_run = t.make_entry_point()
test_run()
