
# Security

## Structure

`Security`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disable_local_ssh` | `bool` | Optional | whether to disable local SSH (by default, local SSH is enabled with allow_mist in Org is enabled |
| `fips_zeroize_password` | `string` | Optional | password required to zeroize devices (FIPS) on site level |
| `limit_ssh_access` | `bool` | Optional | whether to allow certain SSH keys to SSH into the AP (see Site:Setting)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "fips_zeroize_password": "NUKETHESITE",
  "limit_ssh_access": false,
  "disable_local_ssh": false
}
```

