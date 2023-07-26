
# Port Mirror

## Structure

`PortMirror`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `family_type` | `string` | Optional | - |
| `ingress_port_ids` | `List of string` | Optional | - |
| `output_port_id` | `string` | Optional | - |
| `rate` | `int` | Optional | - |
| `run_length` | `int` | Optional | **Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "output_port_id": "ge-0/0/5",
  "family_type": "family_type4",
  "ingress_port_ids": [
    "ingress_port_ids4"
  ],
  "rate": 50,
  "run_length": 58
}
```

