
# Switches 1

## Structure

`Switches1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deviceprofile_id` | `string` | Optional | - |
| `downlink_ips` | `List of string` | Optional | - |
| `downlinks` | `List of string` | Optional | - |
| `esilaglinks` | `List of string` | Optional | - |
| `evpn_id` | `int` | Optional | - |
| `mac` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `pod` | `int` | Optional | optionally, for distribution / access / esilag-access, they can be placed into different pods.<br>e.g.<br><br>* for CLOS, to group dist / access switches into pods<br>* for ERB/CRB, to group dist / esilag-access into pods<br>**Default**: `1`<br>**Constraints**: `>= 1`, `<= 255` |
| `role` | [`Role5Enum`](../../doc/models/role-5-enum.md) | Optional | use `role`==`none` to remove a switch from the topology<br>**Constraints**: *Minimum Length*: `1` |
| `site_id` | `string` | Optional | - |
| `uplinks` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "deviceprofile_id": "6a1deab1-96df-4fa2-8455-d5253f943d06",
  "pod": 1,
  "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
  "downlink_ips": [
    "downlink_ips8",
    "downlink_ips9"
  ],
  "downlinks": [
    "downlinks4"
  ],
  "esilaglinks": [
    "esilaglinks4"
  ],
  "evpn_id": 222
}
```

