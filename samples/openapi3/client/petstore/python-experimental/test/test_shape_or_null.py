# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
try:
    from petstore_api.model import quadrilateral
except ImportError:
    quadrilateral = sys.modules[
        'petstore_api.model.quadrilateral']
try:
    from petstore_api.model import triangle
except ImportError:
    triangle = sys.modules[
        'petstore_api.model.triangle']
from petstore_api.model.shape_or_null import ShapeOrNull


class TestShapeOrNull(unittest.TestCase):
    """ShapeOrNull unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testShapeOrNull(self):
        """Test ShapeOrNull"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ShapeOrNull()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
