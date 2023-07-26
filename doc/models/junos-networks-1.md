
# Junos Networks 1

A network represents a network segment. It can either represent a VLAN (then usually ties to a L3 subnet), optionally associate it with a subnet which can later be used to create addition routes. Used for ports doing `family ethernet-switching`. It can also be a pure L3-subnet that can then be used against a port that with `family inet`.

## Structure

`JunosNetworks1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `gateway` | `string` | Optional | - |
| `ospf_interface_type` | `string` | Optional | - |
| `subnet` | `string` | Optional | optional for pure switching, required when L3 / routing features are used |
| `vlan_id` | `int` | Required | - |
| `zone` | `string` | Optional | used for gateway |

## Example (as JSON)

```json
{
  "dns": [
    "dns1"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ],
  "gateway": "gateway0",
  "ospf_interface_type": "ospf_interface_type4",
  "subnet": "subnet8",
  "vlan_id": 154
}
```

