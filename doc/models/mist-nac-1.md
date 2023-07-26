
# Mist Nac 1

## Structure

`MistNac1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cacerts` | `string` | Optional | the CA certs we use to verify client certs |
| `default_idp_id` | `string` | Optional | use this IDP when no explicit realm present in the incoming username/CN OR when no IDP is explicitly mapped to the incoming realm. |
| `idps` | [`List of Idp`](../../doc/models/idp.md) | Optional | - |
| `server_cert` | [`ServerCert`](../../doc/models/server-cert.md) | Optional | radius server cert to be presented in EAP TLS |

## Example (as JSON)

```json
{
  "cacerts": "-----BEGIN CERTIFICATE-----\\nMIIFZjCCA06gAwIBAgIIP61/1qm/uDowDQYJKoZIhvcNAQELBQE\\n-----END CERTIFICATE-----",
  "default_idp_id": "default_idp_id4",
  "idps": [
    {
      "id": "id7",
      "realm": [
        "realm2",
        "realm3"
      ]
    }
  ],
  "server_cert": {
    "cert": "cert8",
    "key": "key4",
    "password": "password8"
  }
}
```

