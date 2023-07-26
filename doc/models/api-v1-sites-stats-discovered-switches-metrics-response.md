
# Api V1 Sites Stats Discovered Switches Metrics Response

## Structure

`ApiV1SitesStatsDiscoveredSwitchesMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `inactive_wired_vlans` | [`InactiveWiredVlans`](../../doc/models/inactive-wired-vlans.md) | Required | - |
| `poe_compliance` | [`PoeCompliance`](../../doc/models/poe-compliance.md) | Required | - |
| `switch_ap_affinity` | [`SwitchApAffinity`](../../doc/models/switch-ap-affinity.md) | Required | - |
| `version_compliance` | [`VersionCompliance`](../../doc/models/version-compliance.md) | Required | - |

## Example (as JSON)

```json
{
  "inactive_wired_vlans": {
    "details": {
      "key1": "val1",
      "key2": "val2"
    },
    "score": 46.48
  },
  "poe_compliance": {
    "details": {
      "total_aps": 184,
      "total_power": 161.1
    },
    "score": 170.96
  },
  "switch_ap_affinity": {
    "details": {
      "system_name": [
        "system_name4",
        "system_name5"
      ],
      "threshold": 182.02
    },
    "score": 16.64
  },
  "version_compliance": {
    "details": {
      "major_versions": [
        {
          "major_count": 229.24,
          "model": "model2",
          "system_names": [
            "system_names2",
            "system_names3",
            "system_names4"
          ]
        }
      ],
      "total_switch_count": 216
    },
    "score": 149.42
  }
}
```

