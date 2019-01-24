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
    def test_empty_id(self):
        """
        test class in cases of no arguments for id
        """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(4, 3)
        r3 = Rectangle(3, 4)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, r2.id + 1)

    def test_with_id(self):
        """
        test class with id given
        """
        r4 = Rectangle(3, 3, 0, 0, 12)
        r5 = Rectangle(1, 2, 0, 0, 100)
        r6 = Rectangle(2, 1, 0, 0, 10000)
        self.assertEqual(r4.id, 12)
        self.assertEqual(r5.id, 100)
        self.assertEqual(r6.id, 10000)

    def test_mixed_id(self):
        """
        test class with mixed empty and with id
        """
        r7 = Rectangle(1, 1)
        r8 = Rectangle(1, 1, 0, 0, 100)
        r9 = Rectangle(1, 1)
        r10 = Rectangle(1, 1, 0, 0, 200)
        r11 = Rectangle(1, 1)
        self.assertEqual(r8.id, 100)
        self.assertEqual(r9.id, r7.id + 1)
        self.assertEqual(r10.id, 200)
        self.assertEqual(r11.id, r9.id + 1)

    def test_bad_input_id(self):
        """
        test class with unexpected inputs for id
        """
        b1 = Rectangle(1, 1, 1, 1, -1)
        self.assertEqual(b1.id, -1)
        b2 = Rectangle(1, 1, 1, 1, -100)
        self.assertEqual(b2.id, -100)
        b3 = Rectangle(1, 1, 1, 1, float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Rectangle(1, 1, 1, 1, [])
        self.assertEqual(b4.id, [])
        b5 = Rectangle(1, 1, 1, 1, {})
        self.assertEqual(b5.id, {})
        b6 = Rectangle(1, 1, 1, 1, (1,))
        self.assertEqual(b6.id, (1,))
        b7 = Rectangle(1, 1, 1, 1, "Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Rectangle(1, 1, 1, 1, 12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)

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
        """
        test class with wrong values for attributes
        """
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

    def test_area(self):
        """
        test class for area output
        """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(3, 10000)
        self.assertEqual(r1.area(), 30000)

    def test_display(self):
        """
        test class for correct display to stdout
        """
        pass
