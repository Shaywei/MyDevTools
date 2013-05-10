__author__ = 'Shay Weiss'

import os
import unittest

import input_file_parser, juggler_circuit_matcher, output_file_generator

def abs_path_to_test_data_file(file_name):
    return os.path.abspath(os.path.realpath(file_name))

class TestInputFileParser(unittest.TestCase):
    def test_calc_representation_for_output_for_each_juggler(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('juggle_fest_example.txt'))
        circuits, jugglers = input_file_parser.parse_input_file(path_to_test_data)

        # Act
        output_file_generator.calc_representation_for_output_for_each_juggler(circuits, jugglers)

        # Assert
        self.assertEqual('J0 C2:83 C0:104 C1:17,', jugglers[0].representation_for_output)
        self.assertEqual('J1 C0:119 C2:74 C1:18,', jugglers[1].representation_for_output)
        self.assertEqual('J2 C0:128 C2:68 C1:18,', jugglers[2].representation_for_output)
        self.assertEqual('J3 C2:120 C0:171 C1:31,', jugglers[3].representation_for_output)
        self.assertEqual('J4 C0:122 C2:106 C1:23,', jugglers[4].representation_for_output)
        self.assertEqual('J5 C0:161 C2:112 C1:26,', jugglers[5].representation_for_output)
        self.assertEqual('J6 C2:128 C1:31 C0:188,', jugglers[6].representation_for_output)
        self.assertEqual('J7 C2:75 C1:20 C0:106,', jugglers[7].representation_for_output)
        self.assertEqual('J8 C1:21 C0:100 C2:80,', jugglers[8].representation_for_output)
        self.assertEqual('J9 C1:23 C2:86 C0:94,', jugglers[9].representation_for_output)
        self.assertEqual('J10 C0:120 C2:86 C1:21,', jugglers[10].representation_for_output)
        self.assertEqual('J11 C0:154 C1:27 C2:108,', jugglers[11].representation_for_output)

    def test_generate_output_juggle_fest_example(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('juggle_fest_example.txt'))
        circuits, jugglers = input_file_parser.parse_input_file(path_to_test_data)

        matches = juggler_circuit_matcher.matchmaker(juggler_circuit_matcher.jugglers_to_jugglers_prefers(jugglers),
                                                     juggler_circuit_matcher.circuits_to_circuits_prefers(circuits, jugglers))

        output_file_generator.calc_representation_for_output_for_each_juggler(circuits, jugglers)

        expected_output = 'C2 J3 C2:120 C0:171 C1:31, J6 C2:128 C1:31 C0:188, J10 C0:120 C2:86 C1:21, J0 C2:83 C0:104 C1:17\nC1 J8 C1:21 C0:100 C2:80, J9 C1:23 C2:86 C0:94, J1 C0:119 C2:74 C1:18, J7 C2:75 C1:20 C0:106\nC0 J11 C0:154 C1:27 C2:108, J2 C0:128 C2:68 C1:18, J4 C0:122 C2:106 C1:23, J5 C0:161 C2:112 C1:26\n'

        # Act
        actual_output = output_file_generator.generate_output(matches, jugglers)
        output_file_generator.generate_output_file("juggle_fest_example_output.txt", matches, circuits, jugglers)

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_generate_output_juggle_fest(self):
        from datetime import datetime
        time_of_start = datetime.now()
        print 'starting test now (takes about 2 minutes to run): ' + str(time_of_start)
        # Arrange
        print 'starting test'
        path_to_test_data = os.path.abspath(os.path.realpath('juggle_fest.txt'))
        circuits, jugglers = input_file_parser.parse_input_file(path_to_test_data)
        print 'done parsing'
        matches = juggler_circuit_matcher.matchmaker(juggler_circuit_matcher.jugglers_to_jugglers_prefers(jugglers),
                                                     juggler_circuit_matcher.circuits_to_circuits_prefers(circuits, jugglers))
        print 'done matching'
        output_file_generator.calc_representation_for_output_for_each_juggler(circuits, jugglers)
        print 'done calculating output representation for jugglers'
        print 'all that is left is write to file!'
        # Act
        output_file_generator.generate_output_file("juggle_fest_output.txt", matches, circuits, jugglers)

        time_of_finish = datetime.now()
        print 'finishing test now: ' + str(time_of_finish)
        print 'total time for test: ' + str(time_of_finish - time_of_start)

    def test_calc_sum_of_jugglers_names_for_circuit_output_line(self):
        # Arrange
        line = 'C1 J9 C1:23 C2:86 C0:94, J8 C1:21 C0:100 C2:80, J7 C2:75 C1:20 C0:106, J1 C0:119 C2:74 C1:18\n'
        expected_sum = 25

        # Act
        actual_sum = output_file_generator.calc_sum_of_jugglers_names_for_circuit_output_line(line)

        # Assert
        self.assertEqual(expected_sum, actual_sum)

    def test_calc_sum_of_jugglers_names_for_circuit_output_line_for_C1970_in_puzzle(self):
        # Arrange
        line = 'C1970 J4445 C1970:300 C158:200 C1758:190 C1676:130 C1727:160 C802:170 C738:140 C1998:160 C1789:110 C112:150, J6510 C1970:300 C1558:170 C1599:100 C1348:140 C1288:50 C243:170 C289:100 C1067:150 C136:120 C1008:150, J7850 C1970:300 C945:120 C667:150 C1655:230 C1785:210 C1295:80 C223:60 C707:250 C728:170 C1794:160, J2594 C1970:300 C646:100 C1528:210 C887:180 C1799:190 C652:180 C1914:120 C1280:110 C1235:190 C1447:120, J2602 C1970:300 C1921:120 C1504:90 C22:180 C62:240 C1357:90 C1252:80 C1751:150 C332:130 C539:150, J4761 C1970:300 C19:160 C1521:200 C824:220 C141:120 C811:120 C761:190 C1650:120 C1037:100 C371:100'
        expected_sum = 25

        # Act
        print 'mail solution to: ', output_file_generator.calc_sum_of_jugglers_names_for_circuit_output_line(line), '@yodle.com'

if __name__ == '__main__':
    unittest.main()