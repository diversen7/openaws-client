# openaws_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_current_user_v1_users_me_get**](UsersApi.md#users_current_user_v1_users_me_get) | **GET** /v1/users/me | Users:Current User
[**users_list_users_v1_users_get**](UsersApi.md#users_list_users_v1_users_get) | **GET** /v1/users/ | Users:List Users
[**users_patch_current_user_v1_users_me_patch**](UsersApi.md#users_patch_current_user_v1_users_me_patch) | **PATCH** /v1/users/me | Users:Patch Current User
[**users_patch_user_permissions_v1_users_id_permissions_patch**](UsersApi.md#users_patch_user_permissions_v1_users_id_permissions_patch) | **PATCH** /v1/users/{id}/permissions | Users:Patch User Permissions


# **users_current_user_v1_users_me_get**
> UserRead users_current_user_v1_users_me_get()

Users:Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.user_read import UserRead
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
    api_instance = openaws_client.UsersApi(api_client)

    try:
        # Users:Current User
        api_response = api_instance.users_current_user_v1_users_me_get()
        print("The response of UsersApi->users_current_user_v1_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_current_user_v1_users_me_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_users_v1_users_get**
> List[UserRead] users_list_users_v1_users_get(pattern=pattern, limit=limit, offset=offset, order=order, descending=descending, is_active=is_active, is_verified=is_verified, is_employee=is_employee, is_admin=is_admin)

Users:List Users

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.user_read import UserRead
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
    api_instance = openaws_client.UsersApi(api_client)
    pattern = 'pattern_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    order = 'order_example' # str |  (optional)
    descending = False # bool |  (optional) (default to False)
    is_active = True # bool |  (optional)
    is_verified = True # bool |  (optional)
    is_employee = True # bool |  (optional)
    is_admin = True # bool |  (optional)

    try:
        # Users:List Users
        api_response = api_instance.users_list_users_v1_users_get(pattern=pattern, limit=limit, offset=offset, order=order, descending=descending, is_active=is_active, is_verified=is_verified, is_employee=is_employee, is_admin=is_admin)
        print("The response of UsersApi->users_list_users_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_users_v1_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **order** | **str**|  | [optional] 
 **descending** | **bool**|  | [optional] [default to False]
 **is_active** | **bool**|  | [optional] 
 **is_verified** | **bool**|  | [optional] 
 **is_employee** | **bool**|  | [optional] 
 **is_admin** | **bool**|  | [optional] 

### Return type

[**List[UserRead]**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad parameters |  -  |
**403** | Permission denied |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_current_user_v1_users_me_patch**
> UserRead users_patch_current_user_v1_users_me_patch(user_update)

Users:Patch Current User

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.user_read import UserRead
from openaws_client.models.user_update import UserUpdate
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
    api_instance = openaws_client.UsersApi(api_client)
    user_update = openaws_client.UserUpdate() # UserUpdate | 

    try:
        # Users:Patch Current User
        api_response = api_instance.users_patch_current_user_v1_users_me_patch(user_update)
        print("The response of UsersApi->users_patch_current_user_v1_users_me_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_patch_current_user_v1_users_me_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_patch_user_permissions_v1_users_id_permissions_patch**
> UserRead users_patch_user_permissions_v1_users_id_permissions_patch(id, user_update_permissions)

Users:Patch User Permissions

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Api Key Authentication (APIKeyCookie):
```python
import time
import os
import openaws_client
from openaws_client.models.user_read import UserRead
from openaws_client.models.user_update_permissions import UserUpdatePermissions
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
    api_instance = openaws_client.UsersApi(api_client)
    id = None # object | 
    user_update_permissions = openaws_client.UserUpdatePermissions() # UserUpdatePermissions | 

    try:
        # Users:Patch User Permissions
        api_response = api_instance.users_patch_user_permissions_v1_users_id_permissions_patch(id, user_update_permissions)
        print("The response of UsersApi->users_patch_user_permissions_v1_users_id_permissions_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_patch_user_permissions_v1_users_id_permissions_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **user_update_permissions** | [**UserUpdatePermissions**](UserUpdatePermissions.md)|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [APIKeyCookie](../README.md#APIKeyCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Missing token or inactive user. |  -  |
**403** | Permission denied |  -  |
**404** | The user does not exist. |  -  |
**400** | Bad parameters |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

