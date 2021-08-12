'''
案例一：
打开页面（http://sahiteat.com/demo/clicks.htm）
分别对按钮'click me'，'dbl click me'，'right click me'，执行点击、双击、右键操作
打印上面展示框中的内容
'''
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionchains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case(self):
        self.driver.get('http://sahiteat.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()

    def test_case2(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    def test_case3(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()
        #action.click_and_hold(drag_ele).release(drop_ele).perform()
        #action.click_and_hold(drag_ele).move_to_element(drop_ele).release(.perform())
        sleep(4)

    def test_case4(self):
        self.driver.get('http://sahitest.com/demo/labei.htm')
        ele = self.driver.find_element_by_xpath('/hrml/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()



if __name__ == '__main__':
        pytest.main(['-v','-s','web_action.py'])

