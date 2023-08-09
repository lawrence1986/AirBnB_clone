#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import json
import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up test cases."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Cleans up after each test case."""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_initialization(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertTrue(hasattr(self.base_model, 'save'))
        self.assertTrue(hasattr(self.base_model, 'to_dict'))

    def test_attributes_types(self):
        """Test types of BaseModel attributes"""
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        """Test __str__ method of BaseModel"""
        string = str(self.base_model)
        self.assertIn('[BaseModel]', string)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)

    def test_save_method(self):
        """Test save method of BaseModel"""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel"""
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_save_to_file(self):
        """Test save to file"""
        self.base_model.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as file:
            content = file.read()
            self.assertIn('BaseModel', content)
            self.assertIn(self.base_model.id, content)

    def test_reload_from_file(self):
        """Test reload from file"""
        self.base_model.save()
        new_base_model = BaseModel()
        storage.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 2)

    def test_load_attributes_from_dict(self):
        """Test loading attributes from dictionary"""
        base_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_dict)
        self.assertEqual(self.base_model.id, new_base_model.id)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)

    def test_load_attributes_with_datetime(self):
        """Test loading attributes with datetime from dictionary"""
        base_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_dict)
        self.assertEqual(self.base_model.created_at, new_base_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
