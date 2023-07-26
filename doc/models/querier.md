
# Querier

## Structure

`Querier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_response_time` | `int` | Optional | querier’s query response interval, in tenths-of-seconds |
| `mtu` | `int` | Optional | the MTU we use (needed when forming large IGMPv3 Reports) |
| `query_interval` | `int` | Optional | querier’s query interval, in seconds |
| `robustness` | `int` | Optional | querier’s robustness<br>**Constraints**: `>= 1`, `<= 7` |
| `version` | `int` | Optional | querier’s maximum protocol version |

## Example (as JSON)

```json
{
  "max_response_time": 10,
  "mtu": 1500,
  "query_interval": 125,
  "version": 3,
  "robustness": 164
}
```

