import unittest
import pandas as pd
from io import StringIO
from xlsx_processor import process_xlsx

class TestCSVProcessor(unittest.TestCase):
    '''test the process_csv function'''
    def setUp(self):
        # initialize the test data
        self.csv_data = """col_1,col_2,col_3
        1,2,3
        4,,6
        7,8,9
        10,,12
        """
        self.df = pd.read_csv(StringIO(self.csv_data))

    def test_process_csv(self):
        # set the column index to 1
        processed_result = process_xlsx(StringIO(self.csv_data), 1)
        expected_result = """col_1,col_2,col_3
        1,2,3
        7,8,9
        """
        expected_result = pd.read_csv(StringIO(expected_result))

        # check if the result is equal to the expected data
        pd.testing.assert_frame_equal(processed_result, expected_result)

if __name__ == '__main__':
    unittest.main()
    