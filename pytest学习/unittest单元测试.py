import unittest

class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_case1(self):
        print("case1")
        self.assertEqual(1,2,msg="两数判断相等")

    def test_case2(self):
        print("case2")
        self.assertIn("h","there",msg="字母h包含在there单词中")

    #@unittest.skipIf(1+1==2,"跳过此条用例")
    def test_case3(self):
        print("case3")
        self.assertEqual(2, 2, msg="两数判断相等")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")

class demo1(unittest.TestCase):
    def test_demo1_case1(self):
        print("test_demo1_case1")

    def test_demo1_case2(self):
        print("test_demo1_case2")
'''
该执行方式把当前页面中所有以test__开头的用例全部加载出来并执行
if __name__ == '__main__':
        unittest.main()
'''

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case1"))
    suite.addTest(demo1("test_demo1_case1"))
    unittest.TextTestRunner.run(suite)

