
# Tacplus Server 1

## Structure

`TacplusServer1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `host` | `string` | Optional | - |
| `port` | `int` | Optional | - |
| `secret` | `string` | Optional | - |
| `timeout` | `int` | Optional | **Default**: `10`<br>**Constraints**: `>= 1`, `<= 90` |

## Example (as JSON)

```json
{
  "timeout": 10,
  "host": "host8",
  "port": 32,
  "secret": "secret4"
}
```

