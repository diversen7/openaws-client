# coding: utf-8

"""
    Stadsarkivet

    API for Stadsarkivet  # noqa: E501

    The version of the OpenAPI document: 0.6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class BearerResponse(BaseModel):
    """
    BearerResponse
    """
    access_token: StrictStr = Field(...)
    token_type: StrictStr = Field(...)
    __properties = ["access_token", "token_type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BearerResponse:
        """Create an instance of BearerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BearerResponse:
        """Create an instance of BearerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BearerResponse.parse_obj(obj)

        _obj = BearerResponse.parse_obj({
            "access_token": obj.get("access_token"),
            "token_type": obj.get("token_type")
        })
        return _obj

