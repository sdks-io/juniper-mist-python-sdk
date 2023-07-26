
# Api V1 Sites Stats Gateways Metrics Response

## Structure

`ApiV1SitesStatsGatewaysMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config_success` | `float` | Optional | config success score |
| `version_compliance` | [`VersionCompliance1`](../../doc/models/version-compliance-1.md) | Optional | version compliance score, major version for gateway, type |

## Example (as JSON)

```json
{
  "config_success": 99.9,
  "version_compliance": {
    "major_version": {
      "key0": {
        "major_count": 205,
        "major_version": "major_version3"
      },
      "key1": {
        "major_count": 206,
        "major_version": "major_version4"
      },
      "key2": {
        "major_count": 207,
        "major_version": "major_version5"
      }
    },
    "score": 149.42,
    "type": "type2"
  }
}
```

