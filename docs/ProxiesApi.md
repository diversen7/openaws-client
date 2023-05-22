# openaws_client.ProxiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_get_record_v1_records_record_id_get**](ProxiesApi.md#records_get_record_v1_records_record_id_get) | **GET** /v1/records/{record_id} | Records:Get Record
[**records_search_records_v1_records_get**](ProxiesApi.md#records_search_records_v1_records_get) | **GET** /v1/records | Records:Search Records


# **records_get_record_v1_records_record_id_get**
> object records_get_record_v1_records_record_id_get(record_id)

Records:Get Record

### Example

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


# Enter a context with an instance of the API client
with openaws_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openaws_client.ProxiesApi(api_client)
    record_id = 'record_id_example' # str | 

    try:
        # Records:Get Record
        api_response = api_instance.records_get_record_v1_records_record_id_get(record_id)
        print("The response of ProxiesApi->records_get_record_v1_records_record_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxiesApi->records_get_record_v1_records_record_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | ... |  -  |
**400** | ... |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_search_records_v1_records_get**
> object records_search_records_v1_records_get(params=params)

Records:Search Records

### Example

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


# Enter a context with an instance of the API client
with openaws_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openaws_client.ProxiesApi(api_client)
    params = 'params_example' # str |  (optional)

    try:
        # Records:Search Records
        api_response = api_instance.records_search_records_v1_records_get(params=params)
        print("The response of ProxiesApi->records_search_records_v1_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxiesApi->records_search_records_v1_records_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | A bad request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

