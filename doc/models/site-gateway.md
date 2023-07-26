
# Site Gateway

Gateway Site settings

## Structure

`SiteGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_sshkeys` | `List of string` | Optional | for SSR only, as direct root access is not allowed |
| `app_probing` | [`AppProbing1`](../../doc/models/app-probing-1.md) | Optional | - |
| `app_usage` | `bool` | Optional | consumes uplink bandwidth, requires WA license |
| `auto_signature_update` | [`AutoSignatureUpdate`](../../doc/models/auto-signature-update.md) | Optional | - |
| `config_revert_timer` | `float` | Optional | he rollback timer for commit confirmed<br>**Default**: `10`<br>**Constraints**: `>= 1`, `<= 30` |
| `probe_hosts` | `List of string` | Optional | - |
| `root_password` | `string` | Optional | for SRX only |
| `security_log_source_address` | `string` | Optional | - |
| `security_log_source_interface` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "config_revert_timer": 10.0,
  "admin_sshkeys": [
    "admin_sshkeys0",
    "admin_sshkeys1"
  ],
  "app_probing": {
    "apps": [
      "apps8",
      "apps9",
      "apps0"
    ],
    "custom_apps": [
      {
        "app_type": "app_type5",
        "hostname": [
          "hostname9",
          "hostname8"
        ],
        "name": "name1",
        "protocol": "tcp"
      },
      {
        "app_type": "app_type6",
        "hostname": [
          "hostname0"
        ],
        "name": "name2",
        "protocol": "udp"
      }
    ],
    "enabled": false
  },
  "app_usage": false,
  "auto_signature_update": {
    "day_of_week": "day_of_week0",
    "enable": false,
    "time_of_day": "time_of_day6"
  }
}
```

