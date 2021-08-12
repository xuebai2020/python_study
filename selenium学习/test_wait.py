import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)  #隐式等待，全局

    def teardown(self):
        self.driver.quit()

    def testwait(self):

        '''
        直接等待
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        print("hello")
        '''

        '''
        显示等待
        def wait(x):      #自定义函数一定要有一个参数，接参数
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 0
        WebDriverWait(self.driver, 5).until(wait)    #wait传参不要写括号，写括号为调用
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        '''

        '''
        显示等待-py自带的内置方法
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(By.XPATH, '//*[@class="d-button-label"]'))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        '''
