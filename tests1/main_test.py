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
