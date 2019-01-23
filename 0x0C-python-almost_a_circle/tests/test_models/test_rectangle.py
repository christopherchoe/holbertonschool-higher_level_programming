#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
"""
unittest for Rectangle.py
"""


class TestRectangle(unittest.TestCase):
    """
    test class Rectangle for different cases
    """
    def test_empty(self):
        """
        test class in cases of no arguments
        """
        r1 = Rectangle()
        b2 = Rectangle()
        b3 = Rectangle()
        self.assertEqual(r1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_with_id(self):
        """
        test class with id given
        """
        r1 = Rectangle(12)
        b2 = Rectangle(100)
        b3 = Rectangle(10000)
        self.assertEqual(r1.id, 12)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 10000)

    def test_mixed(self):
        """
        test class with mixed empty and with id
        """
        r1 = Rectangle()
        b2 = Rectangle(100)
        b3 = Rectangle()
        b4 = Rectangle(200)
        b5 = Rectangle(0)
        self.assertEqual(r1.id, 4)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 5)
        self.assertEqual(b4.id, 200)
        self.assertEqual(b5.id, 0)

    def test_bad_input(self):
        """
        test class with unexpected inputs
        """
        r1 = Rectangle(-1)
        self.assertEqual(r1.id, -1)
        b2 = Rectangle(-100)
        self.assertEqual(b2.id, -100)
        b3 = Rectangle(float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Rectangle([])
        self.assertEqual(b4.id, [])
        b5 = Rectangle({})
        self.assertEqual(b5.id, {})
        b6 = Rectangle((1,))
        self.assertEqual(b6.id, (1,))
        b7 = Rectangle("Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Rectangle(12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5)

    def test_wrong_type(self):
        """
        test class with wrong type of argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("str", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle([], 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle({}, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, {})

    def test_wrong_values(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -1)
