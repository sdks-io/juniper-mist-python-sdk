
# Passphrase Rules

## Structure

`PassphraseRules`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alphaberts_enabled` | `bool` | Optional | **Default**: `True` |
| `length` | `int` | Optional | **Constraints**: `>= 8`, `<= 63` |
| `max_length` | `int` | Optional | for valid `max_length` and `min_length`, passphrase size is set randomly from that range.<br><br>- if `max_length` and/or `min_length` are invalid, passphrase size is equal to `length` parameter<br>- if `length` is not set or is invalid, default passphrase size is 8.<br>  valid `max_length`, `min_length`, `length` should be an integer between 8 to 63. Also, `max_length` > `min_length`<br>**Constraints**: `>= 8`, `<= 63` |
| `min_length` | `int` | Optional | for valid `max_length` and `min_length`, passphrase size is set randomly from that range.<br><br>- if `max_length` and/or `min_length` are invalid, passphrase size is equal to `length` parameter<br>- if `length` is not set or is invalid, default passphrase size is 8.<br>  valid `max_length`, `min_length`, `length` should be an integer between 8 to 63. Also, `max_length` > `min_length`<br>**Constraints**: `>= 8`, `<= 63` |
| `numerics_enabled` | `bool` | Optional | **Default**: `True` |
| `symbols` | `string` | Optional | - |
| `symbols_enabled` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "alphaberts_enabled": true,
  "numerics_enabled": true,
  "symbols": "()[]{}_%@#&$",
  "symbols_enabled": true,
  "length": 162,
  "max_length": 162,
  "min_length": 98
}
```

