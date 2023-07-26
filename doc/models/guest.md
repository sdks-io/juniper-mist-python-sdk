
# Guest

Guest

## Structure

`Guest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorized` | `bool` | Optional | whether the guest is current authorized |
| `authorized_expiring_time` | `int` | Optional | when the authorization would expire |
| `authorized_time` | `int` | Optional | when the guest was authorized |
| `company` | `string` | Optional | optional, the info provided by user |
| `email` | `string` | Optional | optional, the info provided by user |
| `field_1` | `string` | Optional | optional, the info provided by user |
| `field_2` | `string` | Optional | - |
| `field_3` | `string` | Optional | - |
| `field_4` | `string` | Optional | - |
| `mac` | `string` | Optional | mac |
| `minutes` | `int` | Optional | minutes, the maximum is 259200 (180 days) |
| `name` | `string` | Optional | optional, the info provided by user |
| `ssid` | `string` | Optional | - |
| `wlan_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "authorized_expiring_time": 1480704955,
  "authorized_time": 1480704355,
  "company": "abc",
  "email": "john@abc.com",
  "name": "John Smith",
  "ssid": "Guest-SSID",
  "wlan_id": "6748cfa6-4e12-11e6-9188-0242ac110007",
  "authorized": false
}
```

