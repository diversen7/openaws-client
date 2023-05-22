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
from openaws_client.models.bearer_response import BearerResponse  # noqa: E501
from openaws_client.rest import ApiException

class TestBearerResponse(unittest.TestCase):
    """BearerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BearerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BearerResponse`
        """
        model = openaws_client.models.bearer_response.BearerResponse()  # noqa: E501
        if include_optional :
            return BearerResponse(
                access_token = '', 
                token_type = ''
            )
        else :
            return BearerResponse(
                access_token = '',
                token_type = '',
        )
        """

    def testBearerResponse(self):
        """Test BearerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
