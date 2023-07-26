
# Service Policy 2

## Structure

`ServicePolicy2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Optional | **Default**: `'allow'` |
| `ewf` | [`List of Ewf`](../../doc/models/ewf.md) | Optional | - |
| `idp` | [`JunosIdpConfig`](../../doc/models/junos-idp-config.md) | Optional | - |
| `local_routing` | `bool` | Optional | access within the same VRF<br>**Default**: `False` |
| `name` | `string` | Optional | - |
| `path_preferences` | `string` | Optional | by default, we derive all paths available and use them<br>optionally, you can customize by using `path_preference` |
| `servicepolicy_id` | `uuid\|string` | Optional | used to link servicepolicy defined at org level and overwrite some attributes |
| `services` | `List of string` | Optional | - |
| `tenants` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "action": "allow",
  "local_routing": false,
  "ewf": [
    {
      "alert_only": true,
      "block_message": "block_message9",
      "enabled": true,
      "profille": "standard"
    },
    {
      "alert_only": false,
      "block_message": "block_message0",
      "enabled": false,
      "profille": "strict"
    }
  ],
  "idp": {
    "alert_only": "alert_only2",
    "enabled": false,
    "idpprofile_id": "00000e94-0000-0000-0000-000000000000",
    "profile": "profile8"
  },
  "name": "name0"
}
```

