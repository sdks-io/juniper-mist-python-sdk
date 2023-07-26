
# Wlan 2

## Structure

`Wlan2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth` | `string` | Required | - |
| `bands` | `List of string` | Optional | - |
| `id` | `uuid\|string` | Required | - |
| `ssid` | `string` | Required | - |
| `vlan_ids` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "auth": "auth6",
  "bands": [
    "bands0",
    "bands1"
  ],
  "id": "00001770-0000-0000-0000-000000000000",
  "ssid": "ssid2",
  "vlan_ids": [
    "vlan_ids8",
    "vlan_ids9",
    "vlan_ids0"
  ]
}
```

