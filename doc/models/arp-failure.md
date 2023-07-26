
# Arp Failure

## Structure

`ArpFailure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_count` | `int` | Optional | **Default**: `10` |
| `duration` | `int` | Optional | failing within minutes<br>**Default**: `20`<br>**Constraints**: `>= 5`, `<= 60` |
| `incident_count` | `int` | Optional | **Default**: `10` |

## Example (as JSON)

```json
{
  "client_count": 10,
  "duration": 20,
  "incident_count": 10
}
```

