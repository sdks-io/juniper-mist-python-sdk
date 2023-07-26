
# App Probing 1

## Structure

`AppProbing1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | `List of string` | Optional | - |
| `custom_apps` | [`List of CustomApp`](../../doc/models/custom-app.md) | Optional | - |
| `enabled` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "apps": [
    "apps4",
    "apps5"
  ],
  "custom_apps": [
    {
      "app_type": "app_type1",
      "hostname": [
        "hostname5",
        "hostname6",
        "hostname7"
      ],
      "name": "name7",
      "protocol": "http"
    }
  ],
  "enabled": false
}
```

