from time import sleep

from selenium import webdriver


class Testform():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        #self.driver.quit()
        pass

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys("admin")
        self.driver.find_element_by_id('user_password').send_keys("123")
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_xpath('//*[@id="new_user"/div[4]/input]').click()
        sleep(3)