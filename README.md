# openaws-client
API for Stadsarkivet

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.6.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openaws_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openaws_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = openaws_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Auth:Db Bearer.Login
        api_response = api_instance.auth_db_bearer_login_v1_auth_jwt_login_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_db_bearer_login_v1_auth_jwt_login_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_db_bearer_login_v1_auth_jwt_login_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_db_bearer_login_v1_auth_jwt_login_post**](docs/AuthApi.md#auth_db_bearer_login_v1_auth_jwt_login_post) | **POST** /v1/auth/jwt/login | Auth:Db Bearer.Login
*AuthApi* | [**auth_db_bearer_logout_v1_auth_jwt_logout_post**](docs/AuthApi.md#auth_db_bearer_logout_v1_auth_jwt_logout_post) | **POST** /v1/auth/jwt/logout | Auth:Db Bearer.Logout
*AuthApi* | [**auth_db_cookie_login_v1_auth_login_post**](docs/AuthApi.md#auth_db_cookie_login_v1_auth_login_post) | **POST** /v1/auth/login | Auth:Db Cookie.Login
*AuthApi* | [**auth_db_cookie_logout_v1_auth_logout_post**](docs/AuthApi.md#auth_db_cookie_logout_v1_auth_logout_post) | **POST** /v1/auth/logout | Auth:Db Cookie.Logout
*AuthApi* | [**register_register_v1_auth_register_post**](docs/AuthApi.md#register_register_v1_auth_register_post) | **POST** /v1/auth/register | Register:Register
*AuthApi* | [**reset_forgot_password_v1_auth_forgot_password_post**](docs/AuthApi.md#reset_forgot_password_v1_auth_forgot_password_post) | **POST** /v1/auth/forgot-password | Reset:Forgot Password
*AuthApi* | [**reset_reset_password_v1_auth_reset_password_post**](docs/AuthApi.md#reset_reset_password_v1_auth_reset_password_post) | **POST** /v1/auth/reset-password | Reset:Reset Password
*AuthApi* | [**verify_request_token_v1_auth_request_verify_token_post**](docs/AuthApi.md#verify_request_token_v1_auth_request_verify_token_post) | **POST** /v1/auth/request-verify-token | Verify:Request-Token
*AuthApi* | [**verify_verify_v1_auth_verify_post**](docs/AuthApi.md#verify_verify_v1_auth_verify_post) | **POST** /v1/auth/verify | Verify:Verify
*EntitiesApi* | [**entity_create_entity_v1_entities_post**](docs/EntitiesApi.md#entity_create_entity_v1_entities_post) | **POST** /v1/entities/ | Entity:Create Entity
*EntitiesApi* | [**entity_get_entities_v1_entities_get**](docs/EntitiesApi.md#entity_get_entities_v1_entities_get) | **GET** /v1/entities/ | Entity:Get Entities
*EntitiesApi* | [**entity_get_entity_v1_entities_uuid_get**](docs/EntitiesApi.md#entity_get_entity_v1_entities_uuid_get) | **GET** /v1/entities/{uuid} | Entity:Get Entity
*EntitiesApi* | [**entity_get_entity_version_v1_entities_uuid_versions_id_get**](docs/EntitiesApi.md#entity_get_entity_version_v1_entities_uuid_versions_id_get) | **GET** /v1/entities/{uuid}/versions/{id} | Entity:Get Entity Version
*EntitiesApi* | [**entity_get_entity_versions_v1_entities_uuid_versions_get**](docs/EntitiesApi.md#entity_get_entity_versions_v1_entities_uuid_versions_get) | **GET** /v1/entities/{uuid}/versions | Entity:Get Entity Versions
*EntitiesApi* | [**entity_hard_delete_entity_v1_entities_uuid_hard_delete**](docs/EntitiesApi.md#entity_hard_delete_entity_v1_entities_uuid_hard_delete) | **DELETE** /v1/entities/{uuid}/hard | Entity:Hard Delete Entity
*EntitiesApi* | [**entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete**](docs/EntitiesApi.md#entity_hard_delete_entity_version_v1_entities_uuid_versions_id_delete) | **DELETE** /v1/entities/{uuid}/versions/{id} | Entity:Hard Delete Entity Version
*EntitiesApi* | [**entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch**](docs/EntitiesApi.md#entity_restore_entity_from_soft_deletion_v1_entities_uuid_restore_patch) | **PATCH** /v1/entities/{uuid}/restore | Entity:Restore Entity From Soft Deletion
*EntitiesApi* | [**entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put**](docs/EntitiesApi.md#entity_rollback_to_a_previous_entity_version_v1_entities_uuid_versions_id_rollback_put) | **PUT** /v1/entities/{uuid}/versions/{id}/rollback | Entity:Rollback To A Previous Entity Version
*EntitiesApi* | [**entity_soft_delete_entity_v1_entities_uuid_soft_delete**](docs/EntitiesApi.md#entity_soft_delete_entity_v1_entities_uuid_soft_delete) | **DELETE** /v1/entities/{uuid}/soft | Entity:Soft Delete Entity
*EntitiesApi* | [**entity_update_entity_v1_entities_uuid_patch**](docs/EntitiesApi.md#entity_update_entity_v1_entities_uuid_patch) | **PATCH** /v1/entities/{uuid} | Entity:Update Entity
*ProxiesApi* | [**records_get_record_v1_records_record_id_get**](docs/ProxiesApi.md#records_get_record_v1_records_record_id_get) | **GET** /v1/records/{record_id} | Records:Get Record
*ProxiesApi* | [**records_search_records_v1_records_get**](docs/ProxiesApi.md#records_search_records_v1_records_get) | **GET** /v1/records | Records:Search Records
*SchemasApi* | [**entity_create_schema_v1_schemas_post**](docs/SchemasApi.md#entity_create_schema_v1_schemas_post) | **POST** /v1/schemas/ | Entity:Create Schema
*SchemasApi* | [**entity_get_available_schemas_v1_schemas_get**](docs/SchemasApi.md#entity_get_available_schemas_v1_schemas_get) | **GET** /v1/schemas/ | Entity:Get Available Schemas
*SchemasApi* | [**entity_get_schema_v1_schemas_name_get**](docs/SchemasApi.md#entity_get_schema_v1_schemas_name_get) | **GET** /v1/schemas/{name} | Entity:Get Schema
*UsersApi* | [**users_current_user_v1_users_me_get**](docs/UsersApi.md#users_current_user_v1_users_me_get) | **GET** /v1/users/me | Users:Current User
*UsersApi* | [**users_list_users_v1_users_get**](docs/UsersApi.md#users_list_users_v1_users_get) | **GET** /v1/users/ | Users:List Users
*UsersApi* | [**users_patch_current_user_v1_users_me_patch**](docs/UsersApi.md#users_patch_current_user_v1_users_me_patch) | **PATCH** /v1/users/me | Users:Patch Current User
*UsersApi* | [**users_patch_user_permissions_v1_users_id_permissions_patch**](docs/UsersApi.md#users_patch_user_permissions_v1_users_id_permissions_patch) | **PATCH** /v1/users/{id}/permissions | Users:Patch User Permissions


## Documentation For Models

 - [BearerResponse](docs/BearerResponse.md)
 - [BodyResetForgotPasswordV1AuthForgotPasswordPost](docs/BodyResetForgotPasswordV1AuthForgotPasswordPost.md)
 - [BodyResetResetPasswordV1AuthResetPasswordPost](docs/BodyResetResetPasswordV1AuthResetPasswordPost.md)
 - [BodyVerifyRequestTokenV1AuthRequestVerifyTokenPost](docs/BodyVerifyRequestTokenV1AuthRequestVerifyTokenPost.md)
 - [BodyVerifyVerifyV1AuthVerifyPost](docs/BodyVerifyVerifyV1AuthVerifyPost.md)
 - [Data](docs/Data.md)
 - [Detail](docs/Detail.md)
 - [EntityCreate](docs/EntityCreate.md)
 - [EntityRead](docs/EntityRead.md)
 - [EntityUpdate](docs/EntityUpdate.md)
 - [EntityVersionRead](docs/EntityVersionRead.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [SchemaCreate](docs/SchemaCreate.md)
 - [SchemaRead](docs/SchemaRead.md)
 - [StatusFlag](docs/StatusFlag.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserFlag](docs/UserFlag.md)
 - [UserPermissions](docs/UserPermissions.md)
 - [UserRead](docs/UserRead.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [UserUpdatePermissions](docs/UserUpdatePermissions.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A

<a id="APIKeyCookie"></a>
### APIKeyCookie

- **Type**: API key
- **API key parameter name**: _auth
- **Location**: 


## Author



