
# Password Policy

password policy

## Structure

`PasswordPolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether the policy is enabled<br>**Default**: `False` |
| `freshness` | `int` | Optional | days, required if password policy is enabled |
| `min_length` | `int` | Optional | required password length<br>**Default**: `8` |
| `requires_special_char` | `bool` | Optional | whether to require special character<br>**Default**: `False` |
| `requires_two_factor_auth` | `bool` | Optional | whether to require two-factor auth<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "enabled": false,
  "freshness": 60,
  "min_length": 8,
  "requires_special_char": false,
  "requires_two_factor_auth": false
}
```

