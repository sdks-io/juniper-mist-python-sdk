
# Result 26

## Structure

`Result26`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adopted` | `bool` | Optional | - |
| `aps` | [`List of Aps4`](../../doc/models/aps-4.md) | Optional | **Constraints**: *Unique Items Required* |
| `chassis_id` | `List of string` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `model` | `string` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `system_desc` | `string` | Required | - |
| `system_name` | `string` | Required | - |
| `timestamp` | `float` | Required | - |
| `vendor` | `string` | Required | - |
| `version` | `string` | Required | - |

## Example (as JSON)

```json
{
  "adopted": false,
  "aps": [
    {
      "hostname": "hostname3",
      "mac": "mac5",
      "poe_status": true,
      "port": "port1",
      "port_id": "port_id1"
    },
    {
      "hostname": "hostname2",
      "mac": "mac6",
      "poe_status": false,
      "port": "port2",
      "port_id": "port_id2"
    }
  ],
  "chassis_id": [
    "chassis_id4",
    "chassis_id5",
    "chassis_id6"
  ],
  "for_site": false,
  "model": "model2",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "system_desc": "system_desc6",
  "system_name": "system_name0",
  "timestamp": 128.82,
  "vendor": "vendor6",
  "version": "version4"
}
```

