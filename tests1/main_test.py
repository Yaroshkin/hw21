import unittest
import main

class MyClassTest(unittest.TestCase):
    def test_sum(self):
        num = main.Numbers(1,2,3,4)
        result = num.sumNum()
        self.assertEqual(10, result)

    def test_sred(self):
        num = main.Numbers(1,2,3,4)
        result = num.sredNum()
        self.assertEqual(2.5,result)

    def test_max(self):
        num = main.Numbers(1,2,3,4)
        result = num.maxNum()
        self.assertEqual(4,result)

    def test_min(self):
        num = main.Numbers(1,2,3,4)
        result = num.minNum()
        self.assertEqual(1,result)

    def test_sum(self):
        num = main.Numbers(10,15,25,40)
        result = num.sumNum()
        self.assertEqual(90, result)

    def test_sred(self):
        num = main.Numbers(100,200,300,400)
        result = num.sredNum()
        self.assertEqual(250,result)

    def test_max(self):
        num = main.Numbers(100,2000,323,4685)
        result = num.maxNum()
        self.assertEqual(4685,result)

    def test_min(self):
        num = main.Numbers(1,223,320,4589)
        result = num.minNum()
        self.assertEqual(1,result)

