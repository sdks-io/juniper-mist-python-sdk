
# Wired Client Response

## Structure

`WiredClientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_mac` | `List of string` | Optional | - |
| `device_mac_port` | [`List of DeviceMacPort`](../../doc/models/device-mac-port.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `ip` | `List of string` | Optional | - |
| `mac` | `string` | Optional | - |
| `org_id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `port_id` | `List of string` | Optional | - |
| `site_id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `timestamp` | `float` | Optional | - |
| `vlan` | `List of int` | Optional | - |

## Example (as JSON)

```json
{
  "device_mac": [
    "device_mac1"
  ],
  "device_mac_port": [
    {
      "device_mac": "device_mac0",
      "ip": "ip0",
      "port_id": "port_id6",
      "port_parent": "port_parent8",
      "start": "start0"
    },
    {
      "device_mac": "device_mac1",
      "ip": "ip1",
      "port_id": "port_id7",
      "port_parent": "port_parent9",
      "start": "start1"
    }
  ],
  "ip": [
    "ip1",
    "ip2"
  ],
  "mac": "mac4",
  "org_id": "org_id4"
}
```

