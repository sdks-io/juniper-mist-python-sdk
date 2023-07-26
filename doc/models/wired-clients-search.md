
# Wired Clients Search

## Structure

`WiredClientsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of WiredClientResponse`](../../doc/models/wired-client-response.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "results": [
    {
      "device_mac": [
        "device_mac4"
      ],
      "device_mac_port": [
        {
          "device_mac": "device_mac3",
          "ip": "ip3",
          "port_id": "port_id9",
          "port_parent": "port_parent1",
          "start": "start3"
        },
        {
          "device_mac": "device_mac4",
          "ip": "ip4",
          "port_id": "port_id0",
          "port_parent": "port_parent2",
          "start": "start4"
        }
      ],
      "ip": [
        "ip4",
        "ip5"
      ],
      "mac": "mac7",
      "org_id": "org_id9"
    }
  ],
  "start": 224.84,
  "total": 10,
  "next": "next2"
}
```

