import allure

@allure.link("http://www.baidu.com",name="百度链接")
def test_with_link():
    print("这是一条加类链接的测试")
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK, 'test case title-登录用例')
def test_with_teatcase_link():
    print("这是一条测试用例的链接，链接到你的测试用例里面")
    pass

# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue("140","这是一个issue")
def test_with_issue_link():
    pass

'''
运行带有bug的链接的命令：
pytest allure_issue.py --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{} --alluredir=./results/allure_issue

'''