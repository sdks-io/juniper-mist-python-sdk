
# Trap Group

## Structure

`TrapGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | `List of string` | Optional | - |
| `group_name` | `string` | Optional | Categories list can refer to https://www.juniper.net/documentation/software/topics/task/configuration/snmp-trap-groups-configuring-junos-nm.html |
| `targets` | `List of string` | Optional | - |
| `version` | [`Version1Enum`](../../doc/models/version-1-enum.md) | Optional | **Default**: `'v2'` |

## Example (as JSON)

```json
{
  "group_name": "profiler",
  "version": "v2",
  "categories": [
    "categories4",
    "categories5",
    "categories6"
  ],
  "targets": [
    "targets8",
    "targets9"
  ]
}
```

