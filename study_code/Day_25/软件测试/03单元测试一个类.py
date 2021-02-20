import unittest
import 软件测试.testclass


class mytest(unittest.TestCase):
    def setUp(self):
        self.tclass = 软件测试.myclass.data()  # 实例化测试的类
        pass

    def tearDown(self):
        pass

    def testsum(self):
        self.assertEquals(self.tclass.add(1, 2), 3, "错误")
        pass

    def testsub(self):
        self.assertEquals(self.tclass.sub(1, 2), -1, "错误")
        pass


if __name__ == "__main__":
    unittest.main()
