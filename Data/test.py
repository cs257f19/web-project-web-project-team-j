import unittest
from datasource import *


class MyTestCase(unittest.TestCase)
    def setup(self):
        ds = DataSource()

    def test_getEdited_true(self,ds):
        input = 'TRUE'
        for result in ds.getEdited(input):
            self.assertEqual(result[9],'TRUE')


    def test_getEdited_false(self,ds):
        input = 'FALSE'
        for result in ds.getEdited(input):
            self.assertEqual(result[9],'FALSE')
        pass

    def test_getEdited_otherString(self,ds):
        input = "random"
        self.assertEqual(null)
        pass

    def test_getEdited_notString(self,ds):
        input = 2
        self.assertEqual(null)
        pass

    def test_getEdited_blank(self,ds):
        input = ''
        self.assertEqual(null)
        pass

    def test_getEdited_multinput(self,ds):
        input = list(1,2)
        self.assertEqual(null)
        pass

if __name__ == '__main__':
    unittest.main()
