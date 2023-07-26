
# Neighbors

## Structure

`Neighbors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `export_policy` | `string` | Optional | - |
| `hold_time` | `int` | Optional | **Default**: `90`<br>**Constraints**: `>= 0`, `<= 65535` |
| `import_policy` | `string` | Optional | - |
| `multihop_ttl` | `int` | Optional | assuming BGP neighbor is directly connected<br>**Constraints**: `>= 0`, `<= 255` |
| `neighbor_as` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "hold_time": 90,
  "export_policy": "export_policy0",
  "import_policy": "import_policy4",
  "multihop_ttl": 40,
  "neighbor_as": 210
}
```

