
# Guest 1

information about this portal

## Structure

`Guest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorized` | `bool` | Required | whether this guest is authorized<br>**Default**: `False` |
| `authorized_expiring_time` | `float` | Required | when the guest authorization will expire |
| `authorized_time` | `float` | Required | when the guest is authorized |
| `company` | `string` | Required | - |
| `email` | `string` | Required | - |
| `field_1` | `string` | Required | - |
| `name` | `string` | Required | - |

## Example (as JSON)

```json
{
  "authorized": false,
  "authorized_expiring_time": 93.02,
  "authorized_time": 186.48,
  "company": "company0",
  "email": "email6",
  "field1": "field14",
  "name": "name0"
}
```

