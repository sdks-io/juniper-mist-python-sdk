
# Schedule

WLAN operating schedule, default is disabled

## Structure

`Schedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `hours` | `object` | Optional | time ranges, the key is mon / tue / wed / thu / fri / sat / sun, the value is time range in “HH:MM-HH:MM” (24-hour format), the minimum resolution is 30 minute |

## Example (as JSON)

```json
{
  "enabled": false,
  "hours": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

