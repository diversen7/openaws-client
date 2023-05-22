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
from openaws_client.models.body_reset_reset_password_v1_auth_reset_password_post import BodyResetResetPasswordV1AuthResetPasswordPost  # noqa: E501
from openaws_client.rest import ApiException

class TestBodyResetResetPasswordV1AuthResetPasswordPost(unittest.TestCase):
    """BodyResetResetPasswordV1AuthResetPasswordPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyResetResetPasswordV1AuthResetPasswordPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BodyResetResetPasswordV1AuthResetPasswordPost`
        """
        model = openaws_client.models.body_reset_reset_password_v1_auth_reset_password_post.BodyResetResetPasswordV1AuthResetPasswordPost()  # noqa: E501
        if include_optional :
            return BodyResetResetPasswordV1AuthResetPasswordPost(
                token = '', 
                password = ''
            )
        else :
            return BodyResetResetPasswordV1AuthResetPasswordPost(
                token = '',
                password = '',
        )
        """

    def testBodyResetResetPasswordV1AuthResetPasswordPost(self):
        """Test BodyResetResetPasswordV1AuthResetPasswordPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
