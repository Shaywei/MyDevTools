__author__ = 'ShayWeiss'

import os
from unittest import TestCase

import file_parsers

class TestFileParsers(TestCase):
    def test_parse_line_to_dict(self):
        # Arrange
        expected = [{'num':1, 'num':2, 'num':3,'num_float':1.5, 'num_float':2.5, 'num_float':3.5, 'name':'shay', 'last_name':'weiss'},
                    {'num':10, 'num':20, 'num':30, 'num_float':10.5, 'num_float':20.5, 'num_float':30.5, 'name':'shay2', 'last_name':'weiss2'}]

        path_to_test_data = os.path.abspath(os.path.realpath(os.path.join('TestData', 'dictionary_list_file_parser_test_data.txt')))
        # Act
        result = file_parsers.dictionary_list_file_parser(path_to_test_data, ['num'], ['num_float'])

        # Assert
        self.assertEqual(expected, result)

