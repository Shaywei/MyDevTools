__author__ = 'Shay Weiss'

import unittest

import juggler_circuit_matcher, input_file_parser

class TestJugglerCircuitMatcher(unittest.TestCase):
    def test_juggler_fest_example(self):
        # Arrange
        circuits, jugglers = input_file_parser.parse_input_file("juggle_fest_example.txt")

        jugglers_prefer = juggler_circuit_matcher.jugglers_to_jugglers_prefers(jugglers)
        circuits_prefer = juggler_circuit_matcher.circuits_to_circuits_prefers(circuits, jugglers)

        expected_matches = {'C2': ['J3', 'J6', 'J10', 'J0'], 'C1': ['J8', 'J9', 'J1', 'J7'], 'C0': ['J11', 'J2', 'J4', 'J5']}

        # Act
        actual_matches = juggler_circuit_matcher.matchmaker(jugglers_prefer, circuits_prefer)

        # Assert
        self.assertEqual(expected_matches, actual_matches)

if __name__ == '__main__':
    unittest.main()
