
# Server Cert

radius server cert to be presented in EAP TLS

## Structure

`ServerCert`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cert` | `string` | Optional | - |
| `key` | `string` | Optional | - |
| `password` | `string` | Optional | private key password (optional) |

## Example (as JSON)

```json
{
  "cert": "-----BEGIN CERTIFICATE-----\\nMIIFZjCCA06gAwIBAgIIP61/1qm/uDowDQYJKoZIhvcNAQELBQE\\n-----END CERTIFICATE-----",
  "key": "-----BEGIN PRI...",
  "password": "password4"
}
```

