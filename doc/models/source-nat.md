
# Source Nat

if `routed`==`false` (usually at Spoke), but some hosts needs to be reachable from Hub

## Structure

`SourceNat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exteral_ip` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "exteral_ip": "172.16.0.8/30"
}
```

