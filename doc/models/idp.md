
# Idp

## Structure

`Idp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `realm` | `List of string` | Optional | which realm should trigger this IDP.<br>we extract user realm from<br><br>1. Username-AVP (`mist.com` from john@mist.com)<br>2. Cert CN |

## Example (as JSON)

```json
{
  "id": "4c441a74-d0de-32c4-78a7-a05e00d080ae",
  "realm": [
    "realm5",
    "realm6"
  ]
}
```

