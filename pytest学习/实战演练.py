import allure
import pytest
from selenium import webdriver
import time

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度页面"):
       driver = webdriver.Chrome()
       driver.get("https://www.baidu.com")
       driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
       driver .find_element_by_id("kw").send_keys(test_data1)
       time.sleep(3)
       driver.find_element_by_id("su").click()
       time.sleep(3)

    with allure.step("保存图片"):
        driver.save_screenshot("./results/实战演练.png")
        allure.attach.file("./results/实战演练.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>', 'Attach with type', allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
       driver.quit()