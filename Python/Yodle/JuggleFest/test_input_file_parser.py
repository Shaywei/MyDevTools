__author__ = 'Shay Weiss'

import os
import unittest

import input_file_parser

def abs_path_to_test_data_file(file_name):
    return os.path.abspath(os.path.realpath(file_name))

class TestInputFileParser(unittest.TestCase):
    def test_parse_input_file(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('juggle_fest_example.txt'))

        # Act
        circuits, jugglers = input_file_parser.parse_input_file(path_to_test_data)

        # Assert
        self.assertEqual('C0', circuits[0].name)
        self.assertEqual(7, circuits[0].hep_ranks[0])
        self.assertEqual(7, circuits[0].hep_ranks[1])
        self.assertEqual(10, circuits[0].hep_ranks[2])

        self.assertEqual('C1', circuits[1].name)
        self.assertEqual(2, circuits[1].hep_ranks[0])
        self.assertEqual(1, circuits[1].hep_ranks[1])
        self.assertEqual(1, circuits[1].hep_ranks[2])

        self.assertEqual('C2', circuits[2].name)
        self.assertEqual(7, circuits[2].hep_ranks[0])
        self.assertEqual(6, circuits[2].hep_ranks[1])
        self.assertEqual(4, circuits[2].hep_ranks[2])

        self.assertEqual('J0', jugglers[0].name)
        self.assertEqual(3, jugglers[0].hep_ranks[0])
        self.assertEqual(9, jugglers[0].hep_ranks[1])
        self.assertEqual(2, jugglers[0].hep_ranks[2])
        self.assertEqual(['C2', 'C0', 'C1'], jugglers[0].circuit_preferences)



if __name__ == '__main__':
    unittest.main()