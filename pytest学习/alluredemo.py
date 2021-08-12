import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


'''
方法一
安装python扩展包pip3 install allure-pytest
执行py文件生成测试数据pytest alluredemo.py --alluredir=./results/1
生成测试报告allure serve ./results/1   
生成报告后会自动打开默认的浏览器展示测试报告
------------------------
方法二
allure generate ./results/1 -o ./report/1 --clean
allure open -h 127.0.0.1 -p 8883 ./report/1

'''