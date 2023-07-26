
# Api V1 Sites Devices Check Radius Server Request

## Structure

`ApiV1SitesDevicesCheckRadiusServerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `string` | Required | Specify the password associated with the username |
| `profile` | `string` | Optional | Specify the access profile associated with the subscriber<br>**Default**: `'dot1x'` |
| `user` | `string` | Required | Specify the subscriber username to test |

## Example (as JSON)

```json
{
  "password": "password4",
  "profile": "dot1x",
  "user": "user0"
}
```

