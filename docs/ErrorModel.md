# ErrorModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**Detail**](Detail.md) |  | 

## Example

```python
from openaws_client.models.error_model import ErrorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorModel from a JSON string
error_model_instance = ErrorModel.from_json(json)
# print the JSON string representation of the object
print ErrorModel.to_json()

# convert the object into a dict
error_model_dict = error_model_instance.to_dict()
# create an instance of ErrorModel from a dict
error_model_form_dict = error_model.from_dict(error_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


