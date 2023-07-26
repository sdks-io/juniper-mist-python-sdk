# Self

```python
self_controller = client.self
```

## Class Name

`SelfController`

## Methods

* [Recover Password](../../doc/controllers/self.md#recover-password)
* [Verify Recover Passsword](../../doc/controllers/self.md#verify-recover-passsword)
* [Delete Self](../../doc/controllers/self.md#delete-self)
* [Get Self](../../doc/controllers/self.md#get-self)
* [Update Self](../../doc/controllers/self.md#update-self)
* [List Self Audit Logs](../../doc/controllers/self.md#list-self-audit-logs)
* [List Alarm Subscriptions](../../doc/controllers/self.md#list-alarm-subscriptions)
* [Generate Qr Code for Verification](../../doc/controllers/self.md#generate-qr-code-for-verification)
* [Verify Two Factor](../../doc/controllers/self.md#verify-two-factor)
* [Update Self Email](../../doc/controllers/self.md#update-self-email)
* [Verify Self Email](../../doc/controllers/self.md#verify-self-email)


# Recover Password

Recover Password
An email will also be sent to the user with a link to https://manage.mist.com/verify/recover?token=:token

```python
def recover_password(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1RecoverRequest`](../../doc/models/api-v1-recover-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = ApiV1RecoverRequest(
    email='test@mistsys.com',
    recaptcha='see https://www.google.com/recaptcha/'
)

result = self_controller.recover_password(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Recover401ErrorException`](../../doc/models/api-v1-recover-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Recover403ErrorException`](../../doc/models/api-v1-recover-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Recover404ErrorException`](../../doc/models/api-v1-recover-404-error-exception.md) |


# Verify Recover Passsword

Verify Recover Password
With correct verification, the user will be authenticated. UI can then prompt for new password

```python
def verify_recover_passsword(self,
                            token)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
token = 'token6'

result = self_controller.verify_recover_passsword(token)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1RecoverVerify401ErrorException`](../../doc/models/api-v1-recover-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1RecoverVerify403ErrorException`](../../doc/models/api-v1-recover-verify-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1RecoverVerify404ErrorException`](../../doc/models/api-v1-recover-verify-404-error-exception.md) |


# Delete Self

To delete ones account and every associated with it. The effects:

the account would be deleted
any orphaned Org (that only has this account as admin) will be deleted
along with all data with Org (sites, wlans, devices) will be gone.

```python
def delete_self(self)
```

## Response Type

`object`

## Example Usage

```python
result = self_controller.delete_self()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiV1Self400ErrorException`](../../doc/models/api-v1-self-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1Self401ErrorException`](../../doc/models/api-v1-self-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Self403ErrorException`](../../doc/models/api-v1-self-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Self404ErrorException`](../../doc/models/api-v1-self-404-error-exception.md) |


# Get Self

Get ‘whoami’ and privileges (which org and which sites I have access to)

```python
def get_self(self)
```

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
result = self_controller.get_self()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "admin_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "privileges": [
    {
      "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "msp_name": "string",
      "name": "string",
      "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "org_name": "string",
      "orggroup_ids": [
        "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
      ],
      "role": "admin",
      "scope": "org",
      "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "sitegroup_ids": [
        "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Self401ErrorException`](../../doc/models/api-v1-self-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Self403ErrorException`](../../doc/models/api-v1-self-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Self404ErrorException`](../../doc/models/api-v1-self-404-error-exception.md) |


# Update Self

update Account Information

```python
def update_self(self,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Admin`](../../doc/models/admin.md) | Body, Optional | Request Body |

## Response Type

[`Admin`](../../doc/models/admin.md)

## Example Usage

```python
body = Admin(
    email='john.smith@mycorp.net',
    first_name='John',
    last_name='Smith',
    enable_two_factor=True,
    phone='14081112222',
    phone_2='14083334444'
)

result = self_controller.update_self(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "admin_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "privileges": [
    {
      "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "msp_name": "string",
      "name": "string",
      "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "org_name": "string",
      "orggroup_ids": [
        "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
      ],
      "role": "admin",
      "scope": "org",
      "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "sitegroup_ids": [
        "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Self401ErrorException`](../../doc/models/api-v1-self-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Self403ErrorException`](../../doc/models/api-v1-self-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Self404ErrorException`](../../doc/models/api-v1-self-404-error-exception.md) |


# List Self Audit Logs

Get List of change logs across all Orgs for current admin
Audit logs records all administrative activities done by current admin across all orgs

```python
def list_self_audit_logs(self,
                        page=1,
                        limit=100,
                        start=0,
                        end=0,
                        duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SelfLogsResponse`](../../doc/models/api-v1-self-logs-response.md)

## Example Usage

```python
page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = self_controller.list_self_audit_logs(
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1428954000,
  "limit": 100,
  "page": 1,
  "results": [
    {
      "admin_id": "72bfa2bd-e58a-4670-9d20-a1468f7a6f58",
      "admin_name": "test@mistsys.com",
      "after": {
        "auth": {
          "type": "open"
        }
      },
      "before": {
        "auth": {
          "type": "psk"
        }
      },
      "id": "c6f9347b-b0a4-4a23-b927-fa9249f2ffb2",
      "message": "Update WLAN \"Corporate\"",
      "org_id": "423f6eca-6276-4994-bfeb-53cbbbba6f04",
      "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
      "timestamp": 1431382121
    }
  ],
  "start": 1428939600,
  "total": 135
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfLogs401ErrorException`](../../doc/models/api-v1-self-logs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfLogs403ErrorException`](../../doc/models/api-v1-self-logs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfLogs404ErrorException`](../../doc/models/api-v1-self-logs-404-error-exception.md) |


# List Alarm Subscriptions

Get List of all the subscriptions

```python
def list_alarm_subscriptions(self)
```

## Response Type

[`List of ApiV1SelfSubscriptionsResponse`](../../doc/models/api-v1-self-subscriptions-response.md)

## Example Usage

```python
result = self_controller.list_alarm_subscriptions()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfSubscriptions401ErrorException`](../../doc/models/api-v1-self-subscriptions-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfSubscriptions403ErrorException`](../../doc/models/api-v1-self-subscriptions-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfSubscriptions404ErrorException`](../../doc/models/api-v1-self-subscriptions-404-error-exception.md) |


# Generate Qr Code for Verification

Generate QR code for verification

```python
def generate_qr_code_for_verification(self,
                                     by='qrcode')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `by` | [`ByEnum`](../../doc/models/by-enum.md) | Query, Optional | **Default**: `'qrcode'` |

## Response Type

`object`

## Example Usage

```python
by = ByEnum.QRCODE

result = self_controller.generate_qr_code_for_verification(
    by
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfTwoFactorToken401ErrorException`](../../doc/models/api-v1-self-two-factor-token-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfTwoFactorToken403ErrorException`](../../doc/models/api-v1-self-two-factor-token-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfTwoFactorToken404ErrorException`](../../doc/models/api-v1-self-two-factor-token-404-error-exception.md) |


# Verify Two Factor

Verify Two-factor (OTP)

To verify two-factor authentication by using a code generated by app (e.g. Google Authenticator, Authy) or by SMS. Upon successful verification, the otp_verified will be set to true if it hasn’t already been.

```python
def verify_two_factor(self,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1SelfTwoFactorVerifyRequest`](../../doc/models/api-v1-self-two-factor-verify-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
body = ApiV1SelfTwoFactorVerifyRequest(
    two_factor='123456'
)

result = self_controller.verify_two_factor(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfTwoFactorVerify401ErrorException`](../../doc/models/api-v1-self-two-factor-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfTwoFactorVerify403ErrorException`](../../doc/models/api-v1-self-two-factor-verify-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfTwoFactorVerify404ErrorException`](../../doc/models/api-v1-self-two-factor-verify-404-error-exception.md) |


# Update Self Email

Change Email
We require the user to verify that they actually own the email address they intend to change it to.

After the API call, the user will receive an email to the new email address with a link like https://manage.mist.com/verify/update?expire=:exp_time&email=:admin_email&token=:token

Upon clicking the link, the user is provided with a login page to authenticate using existing credentials. After successful login, the email address of the user gets updated

**Note**: The request parameter email can be used by UI to validate that the current session (if any) belongs to the admin or provide a login page (by pre-populating the email on login screen). UI can also use the request parameter expire to validate token expiry.

```python
def update_self_email(self,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelObjectEmail`](../../doc/models/model-object-email.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
body = ModelObjectEmail(
    email='new@mistsys.com'
)

result = self_controller.update_self_email(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | invalid email address or new email address already exists | [`ApiV1SelfUpdate400ErrorException`](../../doc/models/api-v1-self-update-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1SelfUpdate401ErrorException`](../../doc/models/api-v1-self-update-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfUpdate403ErrorException`](../../doc/models/api-v1-self-update-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfUpdate404ErrorException`](../../doc/models/api-v1-self-update-404-error-exception.md) |


# Verify Self Email

Verify Email change

```python
def verify_self_email(self,
                     token)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
token = 'token6'

result = self_controller.verify_self_email(token)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiV1SelfUpdateVerify400ErrorException`](../../doc/models/api-v1-self-update-verify-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1SelfUpdateVerify401ErrorException`](../../doc/models/api-v1-self-update-verify-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfUpdateVerify403ErrorException`](../../doc/models/api-v1-self-update-verify-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfUpdateVerify404ErrorException`](../../doc/models/api-v1-self-update-verify-404-error-exception.md) |

