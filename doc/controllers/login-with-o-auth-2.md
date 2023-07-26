# Login With O Auth 2

```python
login_with_o_auth_2_controller = client.login_with_o_auth_2
```

## Class Name

`LoginWithOAuth2Controller`

## Methods

* [Unlink O Auth 2 Provider](../../doc/controllers/login-with-o-auth-2.md#unlink-o-auth-2-provider)
* [Get O Auth 2 Authorization Url for Login](../../doc/controllers/login-with-o-auth-2.md#get-o-auth-2-authorization-url-for-login)
* [Login O Auth 2](../../doc/controllers/login-with-o-auth-2.md#login-o-auth-2)
* [Two Factor](../../doc/controllers/login-with-o-auth-2.md#two-factor)
* [Get O Auth 2 Url for Linking](../../doc/controllers/login-with-o-auth-2.md#get-o-auth-2-url-for-linking)
* [Link O Auth 2 Mist Account](../../doc/controllers/login-with-o-auth-2.md#link-o-auth-2-mist-account)


# Unlink O Auth 2 Provider

Unlink OAuth2 Provider

```python
def unlink_o_auth_2_provider(self,
                            provider)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
provider = 'provider8'

result = login_with_o_auth_2_controller.unlink_o_auth_2_provider(provider)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1LoginOauth401ErrorException`](../../doc/models/api-v1-login-oauth-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1LoginOauth403ErrorException`](../../doc/models/api-v1-login-oauth-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1LoginOauth404ErrorException`](../../doc/models/api-v1-login-oauth-404-error-exception.md) |


# Get O Auth 2 Authorization Url for Login

Obtain Authorization URL for Login

```python
def get_o_auth_2_authorization_url_for_login(self,
                                            provider,
                                            forward=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | `string` | Template, Required | - |
| `forward` | `string` | Query, Optional | - |

## Response Type

[`ApiV1LoginOauthResponse`](../../doc/models/api-v1-login-oauth-response.md)

## Example Usage

```python
provider = 'provider8'

forward = 'http://manage.mist.com/oauth/callback.html'

result = login_with_o_auth_2_controller.get_o_auth_2_authorization_url_for_login(
    provider,
    forward
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "authorization_url": "https://accounts.google.com/o/oauth2/v2/auth?.....",
  "client_id": "173131512-mpbnju32.apps.googleusercontent.com"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1LoginOauth401ErrorException`](../../doc/models/api-v1-login-oauth-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1LoginOauth403ErrorException`](../../doc/models/api-v1-login-oauth-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1LoginOauth404ErrorException`](../../doc/models/api-v1-login-oauth-404-error-exception.md) |


# Login O Auth 2

Login via OAuth2

```python
def login_o_auth_2(self,
                  provider,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | `string` | Template, Required | - |
| `body` | [`ApiV1LoginOauthRequest`](../../doc/models/api-v1-login-oauth-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
provider = 'provider8'

body = ApiV1LoginOauthRequest(
    code='4/S9tegDeLkrYg0L9pWNXV4cgMVbbr3SR9t693A2kSHzw'
)

result = login_with_o_auth_2_controller.login_o_auth_2(
    provider,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1LoginOauth401ErrorException`](../../doc/models/api-v1-login-oauth-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1LoginOauth403ErrorException`](../../doc/models/api-v1-login-oauth-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1LoginOauth404ErrorException`](../../doc/models/api-v1-login-oauth-404-error-exception.md) |


# Two Factor

Send 2FA Code

```python
def two_factor(self,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiV1LoginTwoFactorRequest`](../../doc/models/api-v1-login-two-factor-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
body = ApiV1LoginTwoFactorRequest(
    two_factor='123456'
)

result = login_with_o_auth_2_controller.two_factor(
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | two_factor code is incorrect or the user hasn’t login yet | `APIException` |
| 403 | Permission Denied | [`ApiV1LoginTwoFactor403ErrorException`](../../doc/models/api-v1-login-two-factor-403-error-exception.md) |
| 404 | the user doesn’t have 2FA enabled | `APIException` |


# Get O Auth 2 Url for Linking

Obtain Authorization URL for Linking

```python
def get_o_auth_2_url_for_linking(self,
                                provider,
                                forward=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | `string` | Template, Required | - |
| `forward` | `string` | Query, Optional | - |

## Response Type

[`ApiV1SelfOauthResponse`](../../doc/models/api-v1-self-oauth-response.md)

## Example Usage

```python
provider = 'provider8'

forward = 'http://manage.mist.com/oauth/callback.html'

result = login_with_o_auth_2_controller.get_o_auth_2_url_for_linking(
    provider,
    forward
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "authorization_url": "https://accounts.google.com/o/oauth2/v2/auth?.....",
  "linked": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SelfOauth401ErrorException`](../../doc/models/api-v1-self-oauth-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfOauth403ErrorException`](../../doc/models/api-v1-self-oauth-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfOauth404ErrorException`](../../doc/models/api-v1-self-oauth-404-error-exception.md) |


# Link O Auth 2 Mist Account

Link Mist account with an OAuth2 Provider

```python
def link_o_auth_2_mist_account(self,
                              provider,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | `string` | Template, Required | - |
| `body` | [`ApiV1SelfOauthRequest`](../../doc/models/api-v1-self-oauth-request.md) | Body, Optional | Request Body |

## Response Type

[`ApiV1SelfOauthResponse1`](../../doc/models/api-v1-self-oauth-response-1.md)

## Example Usage

```python
provider = 'provider8'

body = ApiV1SelfOauthRequest(
    code='4/S9tegDeLkrYg0L9pWNXV4cgMVbbr3SR9t693A2kSHzw'
)

result = login_with_o_auth_2_controller.link_o_auth_2_mist_account(
    provider,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "action": "oauth account linked",
  "id": "google-user-id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Authorization Error | [`ApiV1SelfOauth400ErrorException`](../../doc/models/api-v1-self-oauth-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1SelfOauth401ErrorException`](../../doc/models/api-v1-self-oauth-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SelfOauth403ErrorException`](../../doc/models/api-v1-self-oauth-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SelfOauth404ErrorException`](../../doc/models/api-v1-self-oauth-404-error-exception.md) |

