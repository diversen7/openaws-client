# EntityVersionRead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**uuid** | **str** |  | 
**status** | [**StatusFlag**](StatusFlag.md) |  | 
**schema_name** | **str** |  | 
**timestamp** | **datetime** |  | 
**updated_by_id** | **str** |  | 
**is_soft_deleted** | **bool** |  | 
**is_hard_deleted** | **bool** |  | 

## Example

```python
from openaws_client.models.entity_version_read import EntityVersionRead

# TODO update the JSON string below
json = "{}"
# create an instance of EntityVersionRead from a JSON string
entity_version_read_instance = EntityVersionRead.from_json(json)
# print the JSON string representation of the object
print EntityVersionRead.to_json()

# convert the object into a dict
entity_version_read_dict = entity_version_read_instance.to_dict()
# create an instance of EntityVersionRead from a dict
entity_version_read_form_dict = entity_version_read.from_dict(entity_version_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


