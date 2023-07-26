
# Junos Port Mirror

## Structure

`JunosPortMirror`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `egress_port_ids` | `List of string` | Optional | at least one of `ingress_port_ids`,`egress_port_ids` or `ingress_networks` should be specified |
| `filter` | `object` | Optional | - |
| `ingress_networks` | `List of string` | Optional | at least one of `ingress_port_ids`,`egress_port_ids` or `ingress_networks` should be specified |
| `ingress_port_ids` | `List of string` | Optional | at least one of `ingress_port_ids`,`egress_port_ids` or `ingress_networks` should be specified |
| `output_network` | `string` | Optional | - |
| `output_port_id` | `string` | Optional | only one of of `output_port_id` or `output_network` should be specified |

## Example (as JSON)

```json
{
  "output_network": "analyze",
  "output_port_id": "ge-0/0/5",
  "egress_port_ids": [
    "egress_port_ids5"
  ],
  "filter": {
    "key1": "val1",
    "key2": "val2"
  },
  "ingress_networks": [
    "ingress_networks8"
  ],
  "ingress_port_ids": [
    "ingress_port_ids4"
  ]
}
```

