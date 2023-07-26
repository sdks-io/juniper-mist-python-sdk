
# Api V1 Sites Rrm Optimize Request

## Structure

`ApiV1SitesRrmOptimizeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bands` | `List of string` | Required | list of bands |
| `macs` | `List of string` | Optional | targeting AP (neighbor APs may get changed, too), default is empty for ALL APs |
| `txpower_only` | `bool` | Optional | only changng TX Power (will not disconnect clients)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "bands": [
    "bands0",
    "bands1"
  ],
  "txpower_only": false,
  "macs": [
    "macs5",
    "macs6"
  ]
}
```

