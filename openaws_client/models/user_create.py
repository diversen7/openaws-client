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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from openaws_client.models.user_flag import UserFlag
from openaws_client.models.user_permissions import UserPermissions

class UserCreate(BaseModel):
    """
    UserCreate
    """
    email: StrictStr = Field(...)
    password: StrictStr = Field(...)
    is_active: Optional[StrictBool] = True
    is_superuser: Optional[StrictBool] = False
    is_verified: Optional[StrictBool] = False
    data: Optional[Dict[str, Any]] = None
    permissions: Optional[UserPermissions] = None
    flags: Optional[UserFlag] = None
    __properties = ["email", "password", "is_active", "is_superuser", "is_verified", "data", "permissions", "flags"]

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
    def from_json(cls, json_str: str) -> UserCreate:
        """Create an instance of UserCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserCreate:
        """Create an instance of UserCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserCreate.parse_obj(obj)

        _obj = UserCreate.parse_obj({
            "email": obj.get("email"),
            "password": obj.get("password"),
            "is_active": obj.get("is_active") if obj.get("is_active") is not None else True,
            "is_superuser": obj.get("is_superuser") if obj.get("is_superuser") is not None else False,
            "is_verified": obj.get("is_verified") if obj.get("is_verified") is not None else False,
            "data": obj.get("data"),
            "permissions": UserPermissions.from_dict(obj.get("permissions")) if obj.get("permissions") is not None else None,
            "flags": obj.get("flags")
        })
        return _obj

