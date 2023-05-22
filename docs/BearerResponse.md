# BearerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from openaws_client.models.bearer_response import BearerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BearerResponse from a JSON string
bearer_response_instance = BearerResponse.from_json(json)
# print the JSON string representation of the object
print BearerResponse.to_json()

# convert the object into a dict
bearer_response_dict = bearer_response_instance.to_dict()
# create an instance of BearerResponse from a dict
bearer_response_form_dict = bearer_response.from_dict(bearer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


