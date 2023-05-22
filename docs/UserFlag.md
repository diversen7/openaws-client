# UserFlag

To check if a user has a flag, use bitmasking: >>> assert user.flags & UserFlag.EMPLOYEE Add a flag: >>> user.flags |= UserFlag.EMPLOYEE Remove a flag: >>> user.flags &= ~UserFlag.EMPLOYEE.  Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


