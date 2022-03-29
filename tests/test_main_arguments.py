import unittest
from src.join import main


class TestArgument(unittest.TestCase):
    def test_without_argument(self):
        argument = []
        self.assertRaises(SystemExit, main, argument)

    def test_with_to_many_argument(self):
        argument = [1, 2, 3, 4, 5]
        self.assertRaises(SystemExit, main, argument)

    def test_first_file_is_not_csv(self):
        f = open("notCsvFile.txt", "w+")
        f.close()
        f = open('left_data.csv', 'w+')
        f.close()
        argument = ['notCsvFile.txt', 'left_data.csv', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_first_file_not_exist(self):
        f = open('left_data.csv', 'w+')
        f.close()
        argument = ['notExistFile.csv', 'left_data.csv', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_second_file_is_not_csv(self):
        f = open("notCsvFile.txt", "w+")
        f.close()
        f = open('left_data.csv', 'w+')
        f.close()
        argument = ['left_data.csv', 'notCsvFile.txt', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_second_file_not_exist(self):
        f = open('left_data.csv', 'w+')
        f.close()
        argument = ['left_data.csv', 'notExistFile.csv', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_join_column_does_not_exist(self):
        f = open('left_data.csv', 'w+')
        f.write("id,header\n")
        f.close()
        f = open('right_data.csv', 'w+')
        f.write("id2,header2\n")
        f.close()
        argument = ['left_data.csv', 'right_data.csv', 'no_header', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_wrong_join_type(self):
        f = open('left_data.csv', 'w+')
        f.write("id,header\n")
        f.close()
        f = open('right_data.csv', 'w+')
        f.write("id,header2\n")
        f.close()
        argument = ['left_data.csv', 'right_data.csv', 'id', 'wrong_join']
        self.assertRaises(SystemExit, main, argument)

    def test_first_empty_file(self):
        f = open('left_data.csv', 'w+')
        f.close()
        f = open('right_data.csv', 'w+')
        f.write("id,header2\n")
        f.close()
        argument = ['left_data.csv', 'right_data.csv', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

    def test_second_empty_file(self):
        f = open('left_data.csv', 'w+')
        f.write("id,header2\n")
        f.close()
        f = open('right_data.csv', 'w+')
        f.close()
        argument = ['left_data.csv', 'right_data.csv', 'id', 'inner']
        self.assertRaises(SystemExit, main, argument)

if __name__ == '__main__':
    unittest.main()
