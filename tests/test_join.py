import unittest
import pandas as pd
import src.join as join


class TestJoin(unittest.TestCase):

    def test_left_join(self):
        left_data = {'id': [1, 2, 3, 4, 5], 'name': ['Patrick', 'Albert', 'Maria', 'Darwin', 'Elizabeth']}
        left_frame = pd.DataFrame(left_data)
        left_frame.to_csv('left_data.csv', index=False)
        right_data = {'id': [3, 1, 1, 6, 4], 'like': ['Stars', 'Climbing', 'Code', 'Rugby', 'Apples']}
        right_data = pd.DataFrame(right_data)
        right_data.to_csv('right_data.csv', index=False)

        test_data = {'id': [1, 1, 2, 3, 4, 5], 'name': ['Patrick', 'Patrick', 'Albert', 'Maria', 'Darwin', 'Elizabeth'],
                     'like': ['Climbing', 'Code', None, 'Stars', 'Apples', None]}
        test_frame = pd.DataFrame(test_data)

        joined = join.left_join('left_data.csv', 'right_data.csv', 'id')

        test_frame = test_frame.sort_values('id').copy()
        joined = joined.sort_values('id').copy()

        test_frame = test_frame.reset_index(drop=True)
        joined = joined.reset_index(drop=True)

        self.assertTrue(test_frame.equals(joined))

    def test_inner_join(self):
        left_data = {'id': [1, 2, 3, 4, 5], 'name': ['Patrick', 'Albert', 'Maria', 'Darwin', 'Elizabeth']}
        left_frame = pd.DataFrame(left_data)
        left_frame.to_csv('left_data.csv', index=False)
        right_data = {'id': [3, 1, 1, 6, 4], 'like': ['Stars', 'Climbing', 'Code', 'Rugby', 'Apples']}
        right_data = pd.DataFrame(right_data)
        right_data.to_csv('right_data.csv', index=False)

        test_data = {'id': [1, 1, 3, 4], 'name': ['Patrick', 'Patrick', 'Maria', 'Darwin'],
                     'like': ['Climbing', 'Code', 'Stars', 'Apples']}
        test_frame = pd.DataFrame(test_data)

        joined = join.inner_join('left_data.csv', 'right_data.csv', 'id')

        test_frame = test_frame.sort_values('id').copy()
        joined = joined.sort_values('id').copy()

        test_frame = test_frame.reset_index(drop=True)
        joined = joined.reset_index(drop=True)

        self.assertTrue(test_frame.equals(joined))

    def test_inner_join_no_null_cells(self):
        left_data = {'id': [1, 2, 3, 4, 5], 'name': ['Patrick', 'Albert', 'Maria', 'Darwin', 'Elizabeth']}
        left_frame = pd.DataFrame(left_data)
        left_frame.to_csv('left_data.csv', index=False)
        right_data = {'id': [3, 1, 1, 6, 4], 'like': ['Stars', 'Climbing', 'Code', 'Rugby', 'Apples']}
        right_data = pd.DataFrame(right_data)
        right_data.to_csv('right_data.csv', index=False)

        joined = join.inner_join('left_data.csv', 'right_data.csv', 'id')

        none_list = []

        for index, row in joined.iterrows():
            none_list.append(any(v is None for v in list(row)))
        self.assertFalse(any(none_list))
