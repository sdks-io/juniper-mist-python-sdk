
# Junos Idp Config

## Structure

`JunosIdpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alert_only` | `string` | Optional | - |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `idpprofile_id` | `uuid\|string` | Optional | org-level IDP Profile can be used, this takes precedence over `profile` |
| `profile` | `string` | Optional | `strict` (default) / `standard` / or keys from from idp_profiles<br>**Default**: `'strict'` |

## Example (as JSON)

```json
{
  "enabled": false,
  "idpprofile_id": "89b9d208-84a4-fa8f-af57-78f92c639cf2",
  "profile": "strict",
  "alert_only": "alert_only0"
}
```

