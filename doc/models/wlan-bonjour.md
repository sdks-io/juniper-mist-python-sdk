
# Wlan Bonjour

bonjour gateway wlan settings

## Structure

`WlanBonjour`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_vlan_ids` | `List of int` | Required | additional VLAN IDs (on the LAN side or from other WLANs) should we be forwarding bonjour queries/responses |
| `enabled` | `bool` | Optional | whether to enable bonjour for this WLAN. Once enabled, limit_bcast is assumed true, allow_mdns is assumed false<br>**Default**: `False` |
| `services` | [`dict`](../../doc/models/services.md) | Required | what services are allowed |

## Example (as JSON)

```json
{
  "additional_vlan_ids": [
    209,
    210,
    211
  ],
  "enabled": false,
  "services": {
    "key0": {
      "disable_local": false,
      "radius_groups": [
        "radius_groups3",
        "radius_groups4"
      ],
      "scope": "scope2"
    },
    "key1": {
      "disable_local": true,
      "radius_groups": [
        "radius_groups2"
      ],
      "scope": "scope1"
    }
  }
}
```

