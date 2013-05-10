__author__ = 'Shay Weiss'

import unittest

import juggler
import circuit

class TestJugglerCircuit(unittest.TestCase):
    def setUp(self):
        self.circuit_under_test1 = circuit.Circuit('C0', [2,3,5])
        self.circuit_under_test2 = circuit.Circuit('C1', [6,3,5])
        self.juggler_under_test = juggler.Juggler('J0', [3,4,6], ['C0', 'C1'])

    def test_sanity(self):
        self.assertEqual('C0', self.circuit_under_test1.name)
        self.assertEqual('C1', self.circuit_under_test2.name)
        self.assertEqual('J0', self.juggler_under_test.name)

        self.assertEqual([2,3,5], self.circuit_under_test1.hep_ranks)
        self.assertEqual([6,3,5], self.circuit_under_test2.hep_ranks)
        self.assertEqual([3,4,6], self.juggler_under_test.hep_ranks)

        self.assertEqual(['C0', 'C1'], self.juggler_under_test.circuit_preferences)

    def test_calc_matches(self):
        # Arrange
        circuits = {}
        circuits.update(self.circuit_under_test1.to_dict())
        circuits.update(self.circuit_under_test2.to_dict())

        # Act
        actual = self.juggler_under_test.calculate_match_to_circuits(circuits)

        # Assert
        self.assertEqual({'C1': 60, 'C0': 48}, self.juggler_under_test.calculate_match_to_circuits())

if __name__ == '__main__':
    unittest.main()