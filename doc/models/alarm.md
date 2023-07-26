
# Alarm

additional information per alarm type

## Structure

`Alarm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ack_admin_id` | `uuid\|string` | Optional | UUID of the admin who acked the alarm |
| `ack_admin_name` | `string` | Optional | Name & Email ID of the admin who acked the alarm |
| `acked` | `bool` | Optional | Whether the alarm is acked or not |
| `acked_time` | `int` | Optional | Epoch (seconds) when the alarm was acked |
| `aps` | `List of string` | Optional | additional information: List of MACs of the APs e.g. [“ffeeddccbbaa”, “ffeeddccbbab”] |
| `bssids` | `List of string` | Optional | List of BSSIDs |
| `count` | `int` | Required | Number of incident within an alarm window |
| `gateways` | `List of string` | Optional | additional information: List of MACs of the gateways e.g. [“ffeeddccbbaa”, “ffeeddccbbab”] |
| `group` | `string` | Required | Group of the alarm |
| `hostnames` | `List of string` | Optional | additional information: List of Hostnames of the devices (AP/Switch/Gateway) |
| `id` | `uuid\|string` | Required | UUID of the alarm |
| `last_seen` | `int` | Required | Epoch (seconds) of the last incident/alarm within an alarm window |
| `note` | `string` | Optional | Text describing the alarm |
| `org_id` | `uuid\|string` | Optional | UUID of the org |
| `severity` | `string` | Required | Severity of the alarm |
| `site_id` | `uuid\|string` | Optional | UUID of the site |
| `ssids` | `List of string` | Optional | List of SSIDs |
| `switches` | `List of string` | Optional | additional information: List of MACs of the switches e.g. [“ffeeddccbbaa”, “ffeeddccbbab”] |
| `timestamp` | `int` | Required | Epoch (seconds) of the first incident/alarm |
| `mtype` | `string` | Required | Key-name of the alarm type |

## Example (as JSON)

```json
{
  "ack_admin_id": "000004b6-0000-0000-0000-000000000000",
  "ack_admin_name": "ack_admin_name8",
  "acked": false,
  "acked_time": 192,
  "aps": [
    "aps1",
    "aps2"
  ],
  "count": 60,
  "group": "group8",
  "id": "00001770-0000-0000-0000-000000000000",
  "last_seen": 42,
  "severity": "severity0",
  "timestamp": 82,
  "type": "type0"
}
```

