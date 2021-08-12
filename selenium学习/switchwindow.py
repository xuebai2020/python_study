'''
多窗口切换
打开百度页面
点击登录
弹框中点击"立即注册"，输入用户名和账号
返回刚才的登录页面，点击登录
输入用户名和恶密码，点击登录
'''
from selenium import webdriver


class TestSwichWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.qiut()

    def test_swichwindow(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.