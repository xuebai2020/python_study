import allure

def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass


def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一个html body块</body>","html测试块",allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/Users/xuebai/desktop/截屏/IMG_0002.png",name='这是一个截屏图片',attachment_type=allure.attachment_type.PNG)





if __name__ == "__main__":
    pytest.main()
'''
执行：
pytest alluredemo1.py --alluredir=./results/alluredemo1 --allure-severities normal,critical

'''