# coding: utf-8

"""
    Stadsarkivet

    API for Stadsarkivet  # noqa: E501

    The version of the OpenAPI document: 0.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openaws_client
from openaws_client.models.schema_read import SchemaRead  # noqa: E501
from openaws_client.rest import ApiException

class TestSchemaRead(unittest.TestCase):
    """SchemaRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SchemaRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaRead`
        """
        model = openaws_client.models.schema_read.SchemaRead()  # noqa: E501
        if include_optional :
            return SchemaRead(
                type = '', 
                data = openaws_client.models.data.Data(), 
                name = '', 
                version = 56, 
                created_by_id = '', 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return SchemaRead(
                type = '',
                data = openaws_client.models.data.Data(),
                name = '',
                version = 56,
                created_by_id = '',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testSchemaRead(self):
        """Test SchemaRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
