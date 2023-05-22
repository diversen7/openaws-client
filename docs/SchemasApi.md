# openaws_client.SchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entity_create_schema_v1_schemas_post**](SchemasApi.md#entity_create_schema_v1_schemas_post) | **POST** /v1/schemas/ | Entity:Create Schema
[**entity_get_available_schemas_v1_schemas_get**](SchemasApi.md#entity_get_available_schemas_v1_schemas_get) | **GET** /v1/schemas/ | Entity:Get Available Schemas
[**entity_get_schema_v1_schemas_name_get**](SchemasApi.md#entity_get_schema_v1_schemas_name_get) | **GET** /v1/schemas/{name} | Entity:Get Schema


# **entity_create_schema_v1_schemas_post**
> SchemaRead entity_create_schema_v1_schemas_post(schema_create)

Entity:Create Schema

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.schema_create import SchemaCreate
from openaws_client.models.schema_read import SchemaRead
from openaws_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openaws_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openaws_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openaws_client.SchemasApi(api_client)
    schema_create = openaws_client.SchemaCreate() # SchemaCreate | 

    try:
        # Entity:Create Schema
        api_response = api_instance.entity_create_schema_v1_schemas_post(schema_create)
        print("The response of SchemasApi->entity_create_schema_v1_schemas_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->entity_create_schema_v1_schemas_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_create** | [**SchemaCreate**](SchemaCreate.md)|  | 

### Return type

[**SchemaRead**](SchemaRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Invalid schema data |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_get_available_schemas_v1_schemas_get**
> List[SchemaRead] entity_get_available_schemas_v1_schemas_get(limit=limit, offset=offset)

Entity:Get Available Schemas

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.schema_read import SchemaRead
from openaws_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openaws_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openaws_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openaws_client.SchemasApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Entity:Get Available Schemas
        api_response = api_instance.entity_get_available_schemas_v1_schemas_get(limit=limit, offset=offset)
        print("The response of SchemasApi->entity_get_available_schemas_v1_schemas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->entity_get_available_schemas_v1_schemas_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[SchemaRead]**](SchemaRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_get_schema_v1_schemas_name_get**
> SchemaRead entity_get_schema_v1_schemas_name_get(name, version=version)

Entity:Get Schema

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.schema_read import SchemaRead
from openaws_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openaws_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyCookie
configuration.api_key['APIKeyCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openaws_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openaws_client.SchemasApi(api_client)
    name = 'name_example' # str | 
    version = 56 # int |  (optional)

    try:
        # Entity:Get Schema
        api_response = api_instance.entity_get_schema_v1_schemas_name_get(name, version=version)
        print("The response of SchemasApi->entity_get_schema_v1_schemas_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->entity_get_schema_v1_schemas_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **version** | **int**|  | [optional] 

### Return type

[**SchemaRead**](SchemaRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Schema not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

