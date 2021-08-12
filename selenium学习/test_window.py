'''
打开百度页面
点击登录
弹框中点击'立即注册'，输入用户名和账号
返回刚才的登录页面，点击登录
输入用户名和密码，点击登录
'''
from time import sleep

from selenium学习.base import Base

class TestWindows(Base):
    def test_login(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        sleep(3)

        #切换新窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username2021gaufuygfge")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("1230000000")
        sleep(3)

        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("17736389500")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("bx19931009")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)





