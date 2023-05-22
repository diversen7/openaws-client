# SchemaRead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | **object** |  | 
**name** | **str** |  | 
**version** | **int** |  | 
**created_by_id** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from openaws_client.models.schema_read import SchemaRead

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRead from a JSON string
schema_read_instance = SchemaRead.from_json(json)
# print the JSON string representation of the object
print SchemaRead.to_json()

# convert the object into a dict
schema_read_dict = schema_read_instance.to_dict()
# create an instance of SchemaRead from a dict
schema_read_form_dict = schema_read.from_dict(schema_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


