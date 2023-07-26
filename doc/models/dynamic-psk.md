
# Dynamic Psk

for dynamic PSK where we get per-user PSK from Radius
dynamic_psk allows PSK to be selected at runtime depending on context (wlan/site/user/...) thus following configurations are assumed (currently)

- PSK will come from RADIUS server
- AP sends client MAC as username ans password (i.e. `enable_mac_auth` is assumed)
- AP sends BSSID:SSID as Caller-Station-ID
- `auth_servers` is required
- PSK will come from cloud WLC if source is cloud_psks
- default_psk will be used if cloud WLC is not available
- `multi_psk_only` and `psk` is ignored
- `pairwise` can only be wpa2-ccmp (for now, wpa3 support on the roadmap)

## Structure

`DynamicPsk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_psk` | `string` | Optional | default PSK to use if cloud WLC is not available, 8-63 characters<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `63` |
| `default_vlan_id` | `int` | Optional | - |
| `enabled` | `bool` | Optional | - |
| `source` | [`Source1Enum`](../../doc/models/source-1-enum.md) | Optional | **Default**: `'radius'` |
| `vlan_ids` | `List of int` | Optional | **Constraints**: `>= 1`, `<= 4094` |

## Example (as JSON)

```json
{
  "source": "radius",
  "default_psk": "default_psk6",
  "default_vlan_id": 30,
  "enabled": false,
  "vlan_ids": [
    196,
    197,
    198
  ]
}
```

