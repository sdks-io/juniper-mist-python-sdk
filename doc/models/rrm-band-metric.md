
# Rrm Band Metric

## Structure

`RrmBandMetric`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cochannel_neighbors` | `float` | Required | average number of co-channel neighbors |
| `density` | `float` | Required | defined by how APs can hear from one and another, 0 - 1 (everyone can hear everyone)<br>**Constraints**: `>= 0`, `<= 1` |
| `neighbors` | `float` | Required | average number of neighbors |
| `noise` | `float` | Required | average noise in dBm |

## Example (as JSON)

```json
{
  "cochannel_neighbors": 244.88,
  "density": 65.5,
  "neighbors": 95.5,
  "noise": 175.8
}
```

