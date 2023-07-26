
# Dns Failure

## Structure

`DnsFailure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_count` | `int` | Optional | **Default**: `20` |
| `duration` | `int` | Optional | failing within minutes<br>**Default**: `10`<br>**Constraints**: `>= 5`, `<= 60` |
| `incident_count` | `int` | Optional | **Default**: `30` |

## Example (as JSON)

```json
{
  "client_count": 20,
  "duration": 10,
  "incident_count": 30
}
```

