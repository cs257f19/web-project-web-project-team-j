import unittest
from datasource import *


class DataSourceTester(unittest.TestCase):

    '''
    Initializes a data source object and forms the connection to the database
    '''
    def setUp(self) -> None:
        self.ds = DataSource()

    #tests the scenario in which user wants comments that are edited, i.e. the tickbox is on
    def test_getEdited_true(self):
        input = 'TRUE'
        for result in self.ds.getEdited(input):
            self.assertEqual(result[9],'TRUE')

    '''
    tests the case in which the user does not want edited comments, i.e. tickbox is off and
    edited == false
    '''
    def test_getEdited_false(self):
        input = 'FALSE'
        for result in self.ds.getEdited(input):
            self.assertEqual(result[9],'FALSE')

    '''
    tests the case in which the input to the get edited function is invalid,
    i.e. a string that is not true or false
    '''
    def test_getEdited_otherString(self):
        input = "random"
        self.assertEqual(self.ds.getEdited(input),None)

    '''
    tests the case in which the invalid input is not a string
    '''
    def test_getEdited_notString(self):
        input = 2
        self.assertEqual(self.ds.getEdited(input),None)

    '''
    tests the case in which the invalid input is a null object or None type
    '''
    def test_getEdited_blank(self):
        input = ''
        self.assertEqual(self.ds.getEdited(input),None)


if __name__ == '__main__':
    unittest.main()
