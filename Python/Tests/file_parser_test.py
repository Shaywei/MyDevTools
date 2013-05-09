__author__ = 'ShayWeiss'

import os
from unittest import TestCase

import file_parsers

def abs_path_to_test_data_file(file_name):
    return os.path.abspath(os.path.realpath(os.path.join('TestData', file_name)))

class TestFileParsers(TestCase):
    def test_dictionary_list_file_parser(self):
        # Arrange
        path_to_test_data = abs_path_to_test_data_file('dictionary_list_file_parser_test_data.txt')

        expected = [{'num':1, 'num':2, 'num':3,'num_float':1.5, 'num_float':2.5, 'num_float':3.5, 'name':'shay', 'last_name':'weiss'},
                    {'num':10, 'num':20, 'num':30, 'num_float':10.5, 'num_float':20.5, 'num_float':30.5, 'name':'shay2', 'last_name':'weiss2'}]

        # Act
        result = file_parsers.dictionary_list_file_parser(path_to_test_data, ['num'], ['num_float'])

        # Assert
        self.assertEqual(expected, result)

    def test_list_of_lists_file_parser_ints(self):
        # Arrange
        path_to_test_data = abs_path_to_test_data_file('list_of_lists_file_parser_ints.txt')
        expected = [[1,2,3],[4,5,6]]

        # Act
        result = file_parsers.list_of_lists_file_parser(path_to_test_data, 'INT')

        # Assert
        self.assertEqual(expected, result)

    def test_list_of_lists_file_parser_floats(self):
        # Arrange
        path_to_test_data = abs_path_to_test_data_file('list_of_lists_file_parser_floats.txt')
        expected = [[1.5,2.5,3.5],[4.5,5.5,6.5]]

        # Act
        result = file_parsers.list_of_lists_file_parser(path_to_test_data, 'FLOAT')

        # Assert
        self.assertEqual(expected, result)

    def test_list_of_lists_file_parser_strings(self):
        # Arrange
        path_to_test_data = abs_path_to_test_data_file('list_of_lists_file_parser_strings.txt')

        expected = [['hi', 'what\'s', 'up'],
                    ['my', 'name', 'is', 'shay'],
                    ['what', 'is', 'yours?']]

        # Act
        result = file_parsers.list_of_lists_file_parser(path_to_test_data)

        # Assert
        self.assertEqual(expected, result)
