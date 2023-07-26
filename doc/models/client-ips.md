
# Client Ips

Property key is the RADIUS Client IP/Subnet.

## Structure

`ClientIps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secret` | `string` | Optional | if different from above |
| `site_id` | `uuid\|string` | Optional | present only for 3rd party clients |
| `vendor` | [`VendorEnum`](../../doc/models/vendor-enum.md) | Optional | convention to be followed is : "<vendor>-<variant>"<br><variant> could be an os/platform/model/company<br>for ex: for cisco vendor, there could variants wrt os (such as ios, nxos etc), platforms (asa etc), or acquired companies (such as meraki, airnonet) etc. |

## Example (as JSON)

```json
{
  "site_id": "00000000-0000-0000-1234-000000000000",
  "vendor": "cisco-ios",
  "secret": "secret4"
}
```

