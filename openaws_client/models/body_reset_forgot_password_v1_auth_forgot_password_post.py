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

class BodyResetForgotPasswordV1AuthForgotPasswordPost(BaseModel):
    """
    BodyResetForgotPasswordV1AuthForgotPasswordPost
    """
    email: StrictStr = Field(...)
    __properties = ["email"]

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
    def from_json(cls, json_str: str) -> BodyResetForgotPasswordV1AuthForgotPasswordPost:
        """Create an instance of BodyResetForgotPasswordV1AuthForgotPasswordPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BodyResetForgotPasswordV1AuthForgotPasswordPost:
        """Create an instance of BodyResetForgotPasswordV1AuthForgotPasswordPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BodyResetForgotPasswordV1AuthForgotPasswordPost.parse_obj(obj)

        _obj = BodyResetForgotPasswordV1AuthForgotPasswordPost.parse_obj({
            "email": obj.get("email")
        })
        return _obj
