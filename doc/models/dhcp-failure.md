
# Dhcp Failure

## Structure

`DhcpFailure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_count` | `int` | Optional | **Default**: `10` |
| `duration` | `int` | Optional | failing within minutes<br>**Default**: `10`<br>**Constraints**: `>= 5`, `<= 60` |
| `incident_count` | `int` | Optional | **Default**: `20` |

## Example (as JSON)

```json
{
  "client_count": 10,
  "duration": 10,
  "incident_count": 20
}
```

