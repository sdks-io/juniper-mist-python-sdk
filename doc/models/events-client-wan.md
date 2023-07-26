
# Events Client Wan

## Structure

`EventsClientWan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `when` | `string` | Optional | - |
| `ev_type` | `string` | Optional | - |
| `metadata` | `object` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `random_mac` | `bool` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `text` | `string` | Optional | - |
| `wcid` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "When": "12/31/2022 23:59:59",
  "ev_type": "CLIENT_IP_ASSIGNED",
  "org_id": "b0b9f142-aaba-11e6-aafc-0242ac110002",
  "site_id": "fc656275-b157-43fd-b922-5f4f341c19bf",
  "text": "DHCP Ack IP 192.168.88.216",
  "wcid": "62bbfb75-10d8-49d1-dec7-d2df91624287",
  "metadata": {
    "key1": "val1",
    "key2": "val2"
  },
  "random_mac": false
}
```

