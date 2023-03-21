import unittest
from main7 import strWork

#
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self): # test method names begin with 'test'
#         self.assertEqual((1 + 2), 4), self.assertEqual(0 + 1, 1)
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0), self.assertEqual((5 * 8), 40)
#
#     if __name__ == '__main__':
#         unittest.main()


class TestMain7(unittest.TestCase):
    def testStrMain7(self):
        self.assertEqual(strWork("Маша мыла раму", "ы"), 1)

    def testStrMain71(self):
        self.assertEqual(strWork("Карл украл у Клары коралл", "л"), 5)

    def testStrMain72(self):
        self.assertEqual(strWork("Лодка плывет по Байкалу", "ю"), 23)
