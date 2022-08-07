#!/usr/bin/python3

"""
test base model
"""

import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime

INSTANCE_DICT = {'id': '859e55ea-63ed-4087-bd02-514dff7df00b',
                 'created_at': '2022-08-03T20:45:21.158641',
                 'updated_at': '2022-08-03T20:45:21.158657',
                 'name': 'My_First_Model', 'my_number': 89,
                 '__class__': 'BaseModel'}

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class MyTestCase(unittest.TestCase):
    """
    Test for Base Model
    """
    def test_initialization(self):
        """
        test for init
        :return: test
        """
        base = BaseModel()
        self.assertIsInstance(base.id, str)  # add assertion here
        self.assertIsInstance(base.created_at, datetime)
        base_2 = BaseModel(**INSTANCE_DICT)
        self.assertIsInstance(base_2, BaseModel)
        self.assertEqual(base_2.created_at, datetime.strptime(INSTANCE_DICT['created_at'], DATE_FORMAT))

    def test_of_to_dict(self):
        """
        test for to_dict()
        """
        base = BaseModel()
        dict_obj = base.to_dict()
        self.assertIsInstance(dict_obj, dict)

    def test_of_save(self):
        """
        test for save()
        """
        base = BaseModel()
        base.save()
        self.assertIsInstance(base.updated_at, datetime)



if __name__ == '__main__':
    unittest.main()
