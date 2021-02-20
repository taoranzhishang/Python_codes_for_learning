def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsum(self):
        self.assertEquals(add(1, 2), 3, "SB不会加法")

    def testsub(self):
        self.assertEquals(sub(3, 1), 2, "SB不会减法")

    def testmul(self):
        self.assertEquals(mul(0, 9), 0, "脑子进水了")


if __name__ == "__main__":
    unittest.main()
