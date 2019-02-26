import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class LoginPage(BaseAction):
    #
     mine_button=By.XPATH,["text,我的","resource-id,com.tpshop.malls:id/mine_txt,1"]
     login_signup_button=By.ID, "com.tpshop.malls:id/head_mimgv"
     username_text_view = By.XPATH, "text,请输入账号"
     password_text_view = By.ID, "com.tpshop.malls:id/pwd_et"
     login_button = By.ID, "com.tpshop.malls:id/login_tv"

     def __init__(self,driver):
         BaseAction.__init__(self,driver)
         self.jump_2_login_page()

     def jump_2_login_page(self):
         # 点击我的
         self.click(self.mine_button)
         # 点击登录/注册
         self.click(self.login_signup_button)

     def input_username(self,text):
         self.input_text(self.username_text_view,text)

     def input_password(self,text):
         self.input_text(self.password_text_view,text)

     def click_login(self):
         self.click(self.login_button)



