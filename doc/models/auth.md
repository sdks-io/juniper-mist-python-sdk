
# Auth

## Structure

`Auth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psk` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Optional | wpa2-AES/CCMPp is assumed when `type`==`psk`<br>**Default**: `'psk'`<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "type": "psk",
  "psk": "psk8"
}
```

