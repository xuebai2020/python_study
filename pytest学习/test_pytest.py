#pytest框架学习
#import pytest


def func(x):
    return x+1

def test_answer():
    assert func(3) == 5


'''
#使用python解释器执行文件
if __name__ == '__main__':
    pytest.main(["test_pytest.py"])
'''