
# Ap Mesh

Mesh AP settings

## Structure

`ApMesh`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether mesh is enabled on this AP<br>**Default**: `False` |
| `group` | `int` | Optional | mesh group, base AP(s) will only allow remote AP(s) in the same mesh group to join, 1-9, optional |
| `role` | [`Role1Enum`](../../doc/models/role-1-enum.md) | Optional | base / remote |

## Example (as JSON)

```json
{
  "enabled": false,
  "group": 182,
  "role": "base"
}
```

