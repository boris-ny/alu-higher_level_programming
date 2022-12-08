#!/usr/bin/python3
'''Unit tests for base.py'''


import os
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestBase (unittest.TestCase):
    '''Class for testing Base class'''

    def test_id(self):
        '''Testing id'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        '''Testing to_json_string method'''
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(Base.to_json_string([{'id': 12}]), str)
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        '''Testing save_to_file method'''
        Base._Base_nb_objects = 0
        Square.save_to_file(None)

        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Rectangle.save_to_file([Rectangle(2, 3)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        '''Testing from_json_string method'''
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(type(Base.from_json_string('[{"id": 89}]')), list)