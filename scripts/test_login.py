import os, sys

import allure
import pytest

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_yml import yml_data_with_filename_and_key


# 数据部分通过yaml/yml
def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    # @pytest.mark.parametrize(("username", "password", "toast"), data_with_key("test_login"))
    # def test_login(self,username,password,toast):
    #
    #     #  输入用户名
    #     self.login_page.input_username(username)
    #     # 输入密码
    #     self.login_page.input_password(password)
    #     # 点击登录
    #     self.login_page.click_login()
    #     assert self.login_page.is_toast_exist(toast)


    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        screen = args["screen"]
        # 输入手机号
        allure.attach('输入用户名', username)
        self.login_page.input_username(username)
        # 输入密码
        allure.attach('输入密码',password)
        self.login_page.input_password(password)
        # 点击登录
        allure.attach('点击登录', '')
        self.login_page.click_login()
        allure.attach('判断成功是否存在',toast)
        res = self.login_page.is_toast_exist(toast, False, screen)
       # assert self.login_page.is_toast_exist(toast)
        # 上传图片
        allure.attach('图片', open('./screen/' + screen + '.png', 'rb').read(), allure.attach_type.PNG)
        assert res

    def teardown(self):
        self.driver.quit()
