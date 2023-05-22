# coding: utf-8

"""
    Stadsarkivet

    API for Stadsarkivet  # noqa: E501

    The version of the OpenAPI document: 0.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class StatusFlag(int, Enum):
    """
    To check if a user has a flag, use bitmasking:  Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
    """

    """
    allowed enum values
    """
    NUMBER_2 = 2
    NUMBER_4 = 4

    @classmethod
    def from_json(cls, json_str: str) -> StatusFlag:
        """Create an instance of StatusFlag from a JSON string"""
        return StatusFlag(json.loads(json_str))


