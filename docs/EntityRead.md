# EntityRead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | 
**schema_name** | **str** |  | 
**id** | **int** |  | 
**uuid** | **str** |  | 
**status** | [**StatusFlag**](StatusFlag.md) |  | 
**timestamp** | **datetime** |  | 
**created_by_id** | **str** |  | 
**updated_by_id** | **str** |  | 
**is_soft_deleted** | **bool** |  | 
**is_hard_deleted** | **bool** |  | 

## Example

```python
from openaws_client.models.entity_read import EntityRead

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRead from a JSON string
entity_read_instance = EntityRead.from_json(json)
# print the JSON string representation of the object
print EntityRead.to_json()

# convert the object into a dict
entity_read_dict = entity_read_instance.to_dict()
# create an instance of EntityRead from a dict
entity_read_form_dict = entity_read.from_dict(entity_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


