import selenium
from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)   #隐式等待

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        self.driver.find_element_by_css_selector(".topic.media.topic-24987").click()
