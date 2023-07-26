
# Installer

## Structure

`Installer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_all_devices` | `bool` | Optional | - |
| `allow_all_sites` | `bool` | Optional | - |
| `extra_site_ids` | `List of uuid\|string` | Optional | - |
| `grace_period` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "allow_all_devices": false,
  "allow_all_sites": false,
  "extra_site_ids": [
    "0000008c-0000-0000-0000-000000000000",
    "0000008d-0000-0000-0000-000000000000"
  ],
  "grace_period": 114.5
}
```

