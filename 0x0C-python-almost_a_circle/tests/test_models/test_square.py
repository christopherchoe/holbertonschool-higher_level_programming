#!/usr/bin/python3
from models.square import Square
import unittest
"""
unittest for Square.py
"""


class TestSquare(unittest.TestCase):
    """
    test class Square for different cases
    """
    def test_empty_id(self):
        """
        test class in cases of no arguments
        """
        s1 = Square(1)
        s2 = Square(2)
        s3 = Square(3)
        self.assertEqual(s2.id, s1.id + 1)
        self.assertEqual(s3.id, s2.id + 1)

    def test_with_id(self):
        """
        test class with id given
        """
        s1 = Square(1, 1, 1, 12)
        s2 = Square(1, 1, 1, 100)
        s3 = Square(1, 1, 1, 10000)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s2.id, 100)
        self.assertEqual(s3.id, 10000)

    def test_mixed(self):
        """
        test class with mixed empty and with id
        """
        s1 = Square(1)
        s2 = Square(1, 1, 1, 100)
        s3 = Square(1)
        s4 = Square(1, 1, 1, 200)
        s5 = Square(1, 1, 1, 0)
        self.assertEqual(s2.id, 100)
        self.assertEqual(s3.id, s1.id + 1)
        self.assertEqual(s4.id, 200)
        self.assertEqual(s5.id, 0)

    def test_bad_input_id(self):
        """
        test class with unexpected inputs
        """
        s1 = Square(1, 1, 1, -1)
        self.assertEqual(s1.id, -1)
        b2 = Square(1, 1, 1, -100)
        self.assertEqual(b2.id, -100)
        b3 = Square(1, 1, 1, float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Square(1, 1, 1, [])
        self.assertEqual(b4.id, [])
        b5 = Square(1, 1, 1, {})
        self.assertEqual(b5.id, {})
        b6 = Square(1, 1, 1, (1,))
        self.assertEqual(b6.id, (1,))
        b7 = Square(1, 1, 1, "Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Square(1, 1, 1, 12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_wrong_type(self):
        """
        test class with wrong type of argument
        """
        with self.assertRaises(TypeError):
            s1 = Square("str", 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, "str")
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, "str")
        with self.assertRaises(TypeError):
            s1 = Square(None, 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, None)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, None)
        with self.assertRaises(TypeError):
            s1 = Square([], 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, [])
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, [])
        with self.assertRaises(TypeError):
            s1 = Square({}, 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, {})
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, {})

    def test_wrong_values(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_area(self):
        """
        test class for area output
        """
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s1 = Square(10000)
        self.assertEqual(s1.area(), 100000000)
