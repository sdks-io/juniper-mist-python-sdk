
# Port Mirroring 1

## Structure

`PortMirroring1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `port_mirror` | [`JunosPortMirror`](../../doc/models/junos-port-mirror.md) | Optional | - |

## Example (as JSON)

```json
{
  "port_mirror": {
    "egress_port_ids": [
      "egress_port_ids9",
      "egress_port_ids0",
      "egress_port_ids1"
    ],
    "filter": {
      "key1": "val1",
      "key2": "val2"
    },
    "ingress_networks": [
      "ingress_networks2",
      "ingress_networks3",
      "ingress_networks4"
    ],
    "ingress_port_ids": [
      "ingress_port_ids8",
      "ingress_port_ids7",
      "ingress_port_ids6"
    ],
    "output_network": "output_network0"
  }
}
```

