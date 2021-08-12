'''
打开百度
先搜索框中输入selenium测试
通过touchaction点击搜索框
滑动到底部，点击下一页
关闭chrome
'''


from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions

class TouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(option=option )
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element_by_id('kw').send_keys("selenium测试")
        ele_search = self.driver.find_element_by_id('su')
        action = TouchActions(self.driver)
        action.tap(ele_search).perform()

        action.scroll_from_element(ele,0,10000).perform()
        sleep(5)

if __name__ == '__main__':
        pytest.main(['-v','-s','web_action.py'])
