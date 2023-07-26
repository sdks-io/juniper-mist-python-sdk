
# Api V1 Sites Stats Switches Metrics Response

## Structure

`ApiV1SitesStatsSwitchesMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active_ports_summary` | [`ActivePortsSummary`](../../doc/models/active-ports-summary.md) | Optional | - |
| `config_success` | [`ConfigSuccess`](../../doc/models/config-success.md) | Optional | - |
| `version_compliance` | [`VersionCompliance2`](../../doc/models/version-compliance-2.md) | Optional | - |

## Example (as JSON)

```json
{
  "active_ports_summary": {
    "details": {
      "active_port_count": 226,
      "total_port_count": 132
    },
    "score": 238,
    "total_switch_count": 26
  },
  "config_success": {
    "details": {
      "config_success_count": 70
    },
    "score": 52,
    "total_switch_count": 160
  },
  "version_compliance": {
    "details": {
      "major_versions": [
        {
          "major_count": 140,
          "major_version": "major_version6",
          "model": "model2",
          "system_names": [
            {
              "key1": "val1",
              "key2": "val2"
            },
            {
              "key1": "val1",
              "key2": "val2"
            },
            {
              "key1": "val1",
              "key2": "val2"
            }
          ]
        }
      ]
    },
    "score": 94,
    "total_switch_count": 138
  }
}
```

