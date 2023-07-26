# Msps SSO

```python
msps_sso_controller = client.msps_sso
```

## Class Name

`MspsSSOController`

## Methods

* [List Msp Ssos](../../doc/controllers/msps-sso.md#list-msp-ssos)
* [Create Msp Sso](../../doc/controllers/msps-sso.md#create-msp-sso)
* [Delete Msp Sso](../../doc/controllers/msps-sso.md#delete-msp-sso)
* [Get Msp Sso](../../doc/controllers/msps-sso.md#get-msp-sso)
* [Update Msp Sso](../../doc/controllers/msps-sso.md#update-msp-sso)
* [List Msp Sso Latest Failures](../../doc/controllers/msps-sso.md#list-msp-sso-latest-failures)
* [Get Msp Sso Saml Metadata](../../doc/controllers/msps-sso.md#get-msp-sso-saml-metadata)
* [Download Msp Sso Saml Metadata](../../doc/controllers/msps-sso.md#download-msp-sso-saml-metadata)


# List Msp Ssos

List MSP SSO Configs

```python
def list_msp_ssos(self,
                 msp_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Sso`](../../doc/models/sso.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.list_msp_ssos(msp_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "custom_logout_url": "string",
    "default_role": "string",
    "domain": "string",
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "idp_cert": "string",
    "idp_sign_algo": "string",
    "idp_sso_url": "string",
    "ignore_unmatched_roles": true,
    "issuer": "string",
    "modified_time": 0,
    "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "nameid_format": "email",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "type": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsos401ErrorException`](../../doc/models/api-v1-msps-ssos-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsos403ErrorException`](../../doc/models/api-v1-msps-ssos-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsos404ErrorException`](../../doc/models/api-v1-msps-ssos-404-error-exception.md) |


# Create Msp Sso

Create MSP SSO profile

```python
def create_msp_sso(self,
                  msp_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Sso`](../../doc/models/sso.md) | Body, Optional | Request Body |

## Response Type

[`Sso`](../../doc/models/sso.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Sso(
    name='name6',
    idp_type=IdpTypeEnum.SAML,
    ldap_type=LdapTypeEnum.AZURE,
    nameid_format=NameidFormatEnum.EMAIL,
    oauth_cc_client_id='e60da615-7def-4c5a-8196-43675f45e174',
    oauth_cc_client_secret='akL8Q~5kWFMVFYl4TFZ3fi~7cMdyDONi6cj01cpH',
    oauth_ropc_client_id='9ce04c97-b5b1-4ec8-af17-f5ed42d2daf7',
    oauth_ropc_secret='blM9R~6kWFMVFYl4TFZ3fi~8cMdyDONi6cj01dqI',
    oauth_tenant_id='dev-88336535',
    oauth_type=OauthTypeEnum.AZURE,
    role_attr_from='role'
)

result = msps_sso_controller.create_msp_sso(
    msp_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "custom_logout_url": "string",
  "default_role": "string",
  "domain": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "idp_cert": "string",
  "idp_sign_algo": "string",
  "idp_sso_url": "string",
  "ignore_unmatched_roles": true,
  "issuer": "string",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "nameid_format": "email",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsos401ErrorException`](../../doc/models/api-v1-msps-ssos-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsos403ErrorException`](../../doc/models/api-v1-msps-ssos-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsos404ErrorException`](../../doc/models/api-v1-msps-ssos-404-error-exception.md) |


# Delete Msp Sso

Delete MSP SSO Config

```python
def delete_msp_sso(self,
                  msp_id,
                  sso_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.delete_msp_sso(
    msp_id,
    sso_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsos401ErrorException`](../../doc/models/api-v1-msps-ssos-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsos403ErrorException`](../../doc/models/api-v1-msps-ssos-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsos404ErrorException`](../../doc/models/api-v1-msps-ssos-404-error-exception.md) |


# Get Msp Sso

Get MSP SSO Config

```python
def get_msp_sso(self,
               msp_id,
               sso_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Sso`](../../doc/models/sso.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.get_msp_sso(
    msp_id,
    sso_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "custom_logout_url": "string",
  "default_role": "string",
  "domain": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "idp_cert": "string",
  "idp_sign_algo": "string",
  "idp_sso_url": "string",
  "ignore_unmatched_roles": true,
  "issuer": "string",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "nameid_format": "email",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsos401ErrorException`](../../doc/models/api-v1-msps-ssos-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsos403ErrorException`](../../doc/models/api-v1-msps-ssos-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsos404ErrorException`](../../doc/models/api-v1-msps-ssos-404-error-exception.md) |


# Update Msp Sso

Update MSP SSO config

```python
def update_msp_sso(self,
                  msp_id,
                  sso_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Sso`](../../doc/models/sso.md) | Body, Optional | Request Body |

## Response Type

[`Sso`](../../doc/models/sso.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Sso(
    name='string',
    custom_logout_url='string',
    idp_cert='string',
    idp_sign_algo='string',
    idp_sso_url='string',
    ignore_unmatched_roles=True,
    issuer='string',
    nameid_format=NameidFormatEnum.EMAIL
)

result = msps_sso_controller.update_msp_sso(
    msp_id,
    sso_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "custom_logout_url": "string",
  "default_role": "string",
  "domain": "string",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "idp_cert": "string",
  "idp_sign_algo": "string",
  "idp_sso_url": "string",
  "ignore_unmatched_roles": true,
  "issuer": "string",
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "nameid_format": "email",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsos401ErrorException`](../../doc/models/api-v1-msps-ssos-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsos403ErrorException`](../../doc/models/api-v1-msps-ssos-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsos404ErrorException`](../../doc/models/api-v1-msps-ssos-404-error-exception.md) |


# List Msp Sso Latest Failures

Get List of MSP SSO Latest Failures

```python
def list_msp_sso_latest_failures(self,
                                msp_id,
                                sso_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`SsoLatestFailures`](../../doc/models/sso-latest-failures.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.list_msp_sso_latest_failures(
    msp_id,
    sso_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "results": [
    {
      "detail": "string",
      "saml_assertion_xml": "string",
      "timestamp": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsosFailures401ErrorException`](../../doc/models/api-v1-msps-ssos-failures-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsosFailures403ErrorException`](../../doc/models/api-v1-msps-ssos-failures-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsosFailures404ErrorException`](../../doc/models/api-v1-msps-ssos-failures-404-error-exception.md) |


# Get Msp Sso Saml Metadata

Get MSP SSO SAML Metadata

```python
def get_msp_sso_saml_metadata(self,
                             msp_id,
                             sso_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`SsoSamlMetadata`](../../doc/models/sso-saml-metadata.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.get_msp_sso_saml_metadata(
    msp_id,
    sso_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "acs_url": "https://api.mist.com/api/v1/saml/llDfa13f/login",
  "entity_id": "https://api.mist.com/api/v1/saml/llDfa13f/login",
  "logout_url": "https://api.mist.com/api/v1/saml/llDfa13f/logout",
  "metadata_xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"https://api.mist.com/api/v1/saml/llDfa13f/login\" validUntil=\"2027-10-12T21:59:01Z\" xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><md:SPSSODescriptor AuthnRequestsSigned=\"false\" WantAssertionsSigned=\"true\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:AssertionConsumerService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://api.mist.com/api/v1/saml/llDfa13f/login\" index=\"0\" isDefault=\"true\"/></md:SPSSODescriptor></md:EntityDescriptor>"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsosMetadata401ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsosMetadata403ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsosMetadata404ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-404-error-exception.md) |


# Download Msp Sso Saml Metadata

Download MSP SSO SAML Metadata

Example of metadata.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?><md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://api.mist.com/api/v1/saml/5hdF5g/login" validUntil="2027-10-12T21:59:01Z" xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <md:SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
        <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://api.mist.com/api/v1/saml/5hdF5g/logout" />
        <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat>
        <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://api.mist.com/api/v1/saml/5hdF5g/login" index="0" isDefault="true"/>
        <md:AttributeConsumingService index="0">
            <md:ServiceName xml:lang="en-US">Mist</md:ServiceName>
            <md:RequestedAttribute Name="Role" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" isRequired="true"/>
            <md:RequestedAttribute Name="FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" isRequired="false"/>
            <md:RequestedAttribute Name="LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" isRequired="false"/>
        </md:AttributeConsumingService>
    </md:SPSSODescriptor>
</md:EntityDescriptor>
```

```python
def download_msp_sso_saml_metadata(self,
                                  msp_id,
                                  sso_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `sso_id` | `uuid\|string` | Template, Required | - |

## Response Type

`string`

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sso_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = msps_sso_controller.download_msp_sso_saml_metadata(
    msp_id,
    sso_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsSsosMetadataXml401ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-xml-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsSsosMetadataXml403ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-xml-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsSsosMetadataXml404ErrorException`](../../doc/models/api-v1-msps-ssos-metadata-xml-404-error-exception.md) |

