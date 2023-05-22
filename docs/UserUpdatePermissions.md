# UserUpdatePermissions

Used to update user permissions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**UserPermissions**](UserPermissions.md) |  | 

## Example

```python
from openaws_client.models.user_update_permissions import UserUpdatePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatePermissions from a JSON string
user_update_permissions_instance = UserUpdatePermissions.from_json(json)
# print the JSON string representation of the object
print UserUpdatePermissions.to_json()

# convert the object into a dict
user_update_permissions_dict = user_update_permissions_instance.to_dict()
# create an instance of UserUpdatePermissions from a dict
user_update_permissions_form_dict = user_update_permissions.from_dict(user_update_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


