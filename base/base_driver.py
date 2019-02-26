import os,sys
sys.path.append(os.getcwd())  # 这两行代码是为了解决 No module named 'base'（系统找不到base目录）
from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    # 解决输入中文问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # toast
    desired_caps['automatorName'] = 'Uiautomator2'
    # 声明driver对象
    driver = webdriver .Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver