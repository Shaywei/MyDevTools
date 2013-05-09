import os
from unittest import TestCase
from Python.Yodle.Triangle import triangle


class TestTriangle(TestCase):
    def test_triangle_example(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('triangle_example.txt'))

        expected = 27

        # Act
        result = triangle.max_path(path_to_test_data)

        # Assert
        self.assertEqual(expected, result)

    def test_triangle_example2(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('triangle_example2.txt'))

        expected = 8 * 9 / 2

        # Act
        result = triangle.max_path(path_to_test_data)

        # Assert
        self.assertEqual(expected, result)

    def test_triangle_example3(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('triangle_example3.txt'))

        expected = 8 * 9 / 2

        # Act
        result = triangle.max_path(path_to_test_data)

        # Assert
        self.assertEqual(expected, result)

    def test_triangle_example4(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('triangle_example4.txt'))

        expected = 1

        # Act
        result = triangle.max_path(path_to_test_data)

        # Assert
        self.assertEqual(expected, result)

    def test_triangle(self):
        # Arrange
        path_to_test_data = os.path.abspath(os.path.realpath('triangle.txt'))

        expected = 1

        # Act
        print triangle.max_path(path_to_test_data)
