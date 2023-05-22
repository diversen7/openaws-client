# openaws_client.EntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entity_create_entity_v1_entities_post**](EntitiesApi.md#entity_create_entity_v1_entities_post) | **POST** /v1/entities/ | Entity:Create Entity
[**entity_get_entities_v1_entities_get**](EntitiesApi.md#entity_get_entities_v1_entities_get) | **GET** /v1/entities/ | Entity:Get Entities
[**entity_get_entity_v1_entities_uuid_get**](EntitiesApi.md#entity_get_entity_v1_entities_uuid_get) | **GET** /v1/entities/{uuid} | Entity:Get Entity
[**entity_get_entity_version_v1_entities_uuid_versions_id_get**](EntitiesApi.md#entity_get_entity_version_v1_entities_uuid_versions_id_get) | **GET** /v1/entities/{uuid}/versions/{id} | Entity:Get Entity Version
[**entity_get_entity_versions_v1_entities_uuid_versions_get**](EntitiesApi.md#entity_get_entity_versions_v1_entities_uuid_versions_get) | **GET** /v1/entities/{uuid}/versions | Entity:Get Entity Versions
[**entity_hard_delete_entity_v1_entities_uuid_hard_delete**](EntitiesApi.md#entity_hard_delete_entity_v1_entities_uuid_hard_delete) | **DELETE** /v1/entities/{uuid}/hard | Entity:Hard Delete Entity
[**entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete**](EntitiesApi.md#entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete) | **DELETE** /v1/entities/{uuid}/versions/{id} | Entity:Hard Delete Entity Version
[**entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch**](EntitiesApi.md#entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch) | **PATCH** /v1/entities/{uuid}/restore | Entity:Restore Entity From Soft Deletion
[**entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put**](EntitiesApi.md#entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put) | **PUT** /v1/entities/{uuid}/versions/{id}/rollback | Entity:Rollback To A Previous Entity Version
[**entity_soft_delete_entity_v1_entities_uuid_soft_delete**](EntitiesApi.md#entity_soft_delete_entity_v1_entities_uuid_soft_delete) | **DELETE** /v1/entities/{uuid}/soft | Entity:Soft Delete Entity
[**entity_update_entity_v1_entities_uuid_patch**](EntitiesApi.md#entity_update_entity_v1_entities_uuid_patch) | **PATCH** /v1/entities/{uuid} | Entity:Update Entity


# **entity_create_entity_v1_entities_post**
> EntityRead entity_create_entity_v1_entities_post(entity_create)

Entity:Create Entity

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_create import EntityCreate
from openaws_client.models.entity_read import EntityRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    entity_create = openaws_client.EntityCreate() # EntityCreate | 

    try:
        # Entity:Create Entity
        api_response = api_instance.entity_create_entity_v1_entities_post(entity_create)
        print("The response of EntitiesApi->entity_create_entity_v1_entities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_create_entity_v1_entities_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_create** | [**EntityCreate**](EntityCreate.md)|  | 

### Return type

[**EntityRead**](EntityRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Invalid entity data |  -  |
**403** | Permission denied |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_get_entities_v1_entities_get**
> List[EntityRead] entity_get_entities_v1_entities_get(offset=offset, limit=limit)

Entity:Get Entities

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_read import EntityRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Entity:Get Entities
        api_response = api_instance.entity_get_entities_v1_entities_get(offset=offset, limit=limit)
        print("The response of EntitiesApi->entity_get_entities_v1_entities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_get_entities_v1_entities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[EntityRead]**](EntityRead.md)

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

# **entity_get_entity_v1_entities_uuid_get**
> EntityRead entity_get_entity_v1_entities_uuid_get(uuid)

Entity:Get Entity

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_read import EntityRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Entity:Get Entity
        api_response = api_instance.entity_get_entity_v1_entities_uuid_get(uuid)
        print("The response of EntitiesApi->entity_get_entity_v1_entities_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_get_entity_v1_entities_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**EntityRead**](EntityRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_get_entity_version_v1_entities_uuid_versions_id_get**
> EntityRead entity_get_entity_version_v1_entities_uuid_versions_id_get(uuid, id)

Entity:Get Entity Version

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_read import EntityRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 
    id = 56 # int | 

    try:
        # Entity:Get Entity Version
        api_response = api_instance.entity_get_entity_version_v1_entities_uuid_versions_id_get(uuid, id)
        print("The response of EntitiesApi->entity_get_entity_version_v1_entities_uuid_versions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_get_entity_version_v1_entities_uuid_versions_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**EntityRead**](EntityRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_get_entity_versions_v1_entities_uuid_versions_get**
> List[EntityVersionRead] entity_get_entity_versions_v1_entities_uuid_versions_get(uuid, limit=limit, offset=offset)

Entity:Get Entity Versions

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_version_read import EntityVersionRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 
    limit = 10 # int |  (optional) (default to 10)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Entity:Get Entity Versions
        api_response = api_instance.entity_get_entity_versions_v1_entities_uuid_versions_get(uuid, limit=limit, offset=offset)
        print("The response of EntitiesApi->entity_get_entity_versions_v1_entities_uuid_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_get_entity_versions_v1_entities_uuid_versions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[EntityVersionRead]**](EntityVersionRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_hard_delete_entity_v1_entities_uuid_hard_delete**
> int entity_hard_delete_entity_v1_entities_uuid_hard_delete(uuid)

Entity:Hard Delete Entity

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Entity:Hard Delete Entity
        api_response = api_instance.entity_hard_delete_entity_v1_entities_uuid_hard_delete(uuid)
        print("The response of EntitiesApi->entity_hard_delete_entity_v1_entities_uuid_hard_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_hard_delete_entity_v1_entities_uuid_hard_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

**int**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**403** | Permission denied |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete**
> int entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete(uuid, id)

Entity:Hard Delete Entity Version

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 
    id = 56 # int | 

    try:
        # Entity:Hard Delete Entity Version
        api_response = api_instance.entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete(uuid, id)
        print("The response of EntitiesApi->entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **id** | **int**|  | 

### Return type

**int**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**403** | Permission denied |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch**
> EntityVersionRead entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch(uuid)

Entity:Restore Entity From Soft Deletion

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_version_read import EntityVersionRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Entity:Restore Entity From Soft Deletion
        api_response = api_instance.entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch(uuid)
        print("The response of EntitiesApi->entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**EntityVersionRead**](EntityVersionRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put**
> EntityRead entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put(uuid, id)

Entity:Rollback To A Previous Entity Version

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_read import EntityRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 
    id = 56 # int | 

    try:
        # Entity:Rollback To A Previous Entity Version
        api_response = api_instance.entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put(uuid, id)
        print("The response of EntitiesApi->entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**EntityRead**](EntityRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_soft_delete_entity_v1_entities_uuid_soft_delete**
> EntityVersionRead entity_soft_delete_entity_v1_entities_uuid_soft_delete(uuid)

Entity:Soft Delete Entity

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_version_read import EntityVersionRead
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Entity:Soft Delete Entity
        api_response = api_instance.entity_soft_delete_entity_v1_entities_uuid_soft_delete(uuid)
        print("The response of EntitiesApi->entity_soft_delete_entity_v1_entities_uuid_soft_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_soft_delete_entity_v1_entities_uuid_soft_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**EntityVersionRead**](EntityVersionRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**403** | Permission denied |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_update_entity_v1_entities_uuid_patch**
> EntityRead entity_update_entity_v1_entities_uuid_patch(uuid, entity_update)

Entity:Update Entity

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.entity_read import EntityRead
from openaws_client.models.entity_update import EntityUpdate
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
    api_instance = openaws_client.EntitiesApi(api_client)
    uuid = 'uuid_example' # str | 
    entity_update = openaws_client.EntityUpdate() # EntityUpdate | 

    try:
        # Entity:Update Entity
        api_response = api_instance.entity_update_entity_v1_entities_uuid_patch(uuid, entity_update)
        print("The response of EntitiesApi->entity_update_entity_v1_entities_uuid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entity_update_entity_v1_entities_uuid_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **entity_update** | [**EntityUpdate**](EntityUpdate.md)|  | 

### Return type

[**EntityRead**](EntityRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Entity not found |  -  |
**403** | Permission denied |  -  |
**400** | Invalid UUID |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

