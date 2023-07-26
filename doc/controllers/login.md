# Login

```python
login_controller = client.login
```

## Class Name

`LoginController`

## Methods

* [Login](../../doc/controllers/login.md#login)
* [Lookup](../../doc/controllers/login.md#lookup)
* [Logout](../../doc/controllers/login.md#logout)


# Login

Log in with email/password.
When 2FA is enabled, there are two ways to login:

1. login with two_factor token (with Google Authenticator, etc)
2. login with email/password, generate the token, and use /login/two_factor with the token

```python
def login(self,
         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1LoginRequest`](../../doc/models/api-v1-login-request.md) | Body, Optional | - |

## Response Type

[`ApiV1LoginResponse`](../../doc/models/api-v1-login-response.md)

## Example Usage

```python
body = ApiV1LoginRequest(
    email='string',
    password='string',
    two_factor='string'
)

result = login_controller.login(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "email": "test@mistsys.com",
  "two_factor_passed": false,
  "two_factor_required": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Login Failed | [`ApiV1Login400ErrorException`](../../doc/models/api-v1-login-400-error-exception.md) |


# Lookup

Login Lookup

```python
def lookup(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModelObjectEmail`](../../doc/models/model-object-email.md) | Body, Optional | Request Body |

## Response Type

[`ApiV1LoginLookupResponse`](../../doc/models/api-v1-login-lookup-response.md)

## Example Usage

```python
body = ModelObjectEmail(
    email='test@mistsys.com'
)

result = login_controller.lookup(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "sso_url": "https://my.sso/idp_sso_url"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1LoginLookup401ErrorException`](../../doc/models/api-v1-login-lookup-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1LoginLookup403ErrorException`](../../doc/models/api-v1-login-lookup-403-error-exception.md) |
| 404 | user does not exist | `APIException` |


# Logout

Logout

```python
def logout(self)
```

## Response Type

[`ApiV1LogoutResponse`](../../doc/models/api-v1-logout-response.md)

## Example Usage

```python
result = login_controller.logout()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "forward_url": "https://my.sso/custom_logout_url"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Logout401ErrorException`](../../doc/models/api-v1-logout-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Logout403ErrorException`](../../doc/models/api-v1-logout-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Logout404ErrorException`](../../doc/models/api-v1-logout-404-error-exception.md) |

