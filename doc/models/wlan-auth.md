
# Wlan Auth

authentication wlan settings

## Structure

`WlanAuth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `anticlog_threshold` | `int` | Optional | SAE anti-clogging token threshold<br>**Default**: `16`<br>**Constraints**: `>= 16`, `<= 32` |
| `eap_reauth` | `bool` | Optional | whether to trigger EAP reauth when the session ends<br>**Default**: `False` |
| `enable_mac_auth` | `bool` | Optional | whether to enable MAC Auth, uses the same auth_servers<br>**Default**: `False` |
| `key_idx` | `int` | Optional | when type=wep<br>**Default**: `1`<br>**Constraints**: `>= 1`, `<= 4` |
| `keys` | `List of string` | Optional | when type=wep, four 10-character or 26-character hex string, null can be used. All keys, if provided, have to be in the same length |
| `multi_psk_only` | `bool` | Optional | whether to only use multi_psk<br>**Default**: `False` |
| `owe` | `string` | Optional | - |
| `pairwise` | `List of string` | Optional | when type=psk / eap, one or more of wpa2-ccmp / wpa1-tkip / wpa1-ccmp / wpa2-tkip |
| `private_wlan` | `bool` | Optional | whether private wlan is enabled. only applicable to multi_psk mode |
| `psk` | `string` | Optional | when type=psk, 8-64 characters, or 64 hex characters<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `64` |
| `mtype` | [`Type38Enum`](../../doc/models/type-38-enum.md) | Required | **Default**: `'open'` |
| `wep_as_secondary_auth` | `bool` | Optional | enable WEP as secondary auth |

## Example (as JSON)

```json
{
  "anticlog_threshold": 16,
  "eap_reauth": false,
  "enable_mac_auth": false,
  "key_idx": 1,
  "multi_psk_only": false,
  "pairwise": null,
  "type": "open",
  "keys": [
    "keys8"
  ]
}
```

