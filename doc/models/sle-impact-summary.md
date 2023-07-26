
# Sle Impact Summary

## Structure

`SleImpactSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | [`List of Ap`](../../doc/models/ap.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `band` | [`List of Band9`](../../doc/models/band-9.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `classifier` | `string` | Required | - |
| `device_os` | [`List of DeviceO`](../../doc/models/device-o.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `device_type` | [`List of DeviceType`](../../doc/models/device-type.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `end` | `float` | Required | - |
| `failure` | `string` | Required | - |
| `metric` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `start` | `float` | Required | - |
| `wlan` | [`List of Wlan1`](../../doc/models/wlan-1.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "ap": [
    {
      "ap_mac": "ap_mac4",
      "degraded": 252.52,
      "duration": 125.58,
      "name": "name2",
      "total": 231.48
    }
  ],
  "band": [
    {
      "band": "band5",
      "degraded": 197.23,
      "duration": 70.29,
      "name": "name3",
      "total": 225.23
    }
  ],
  "classifier": "classifier4",
  "device_os": [
    {
      "degraded": 91.2,
      "device_os": "device_os0",
      "duration": 220.26,
      "name": "name0",
      "total": 119.2
    }
  ],
  "device_type": [
    {
      "degraded": 115.9,
      "device_type": "device_type0",
      "duration": 244.96,
      "name": "name0",
      "total": 112.1
    }
  ],
  "end": 12.78,
  "failure": "failure6",
  "metric": "metric8",
  "start": 224.84,
  "wlan": [
    {
      "degraded": 134.9,
      "duration": 7.96,
      "name": "name0",
      "total": 93.1,
      "wlan_id": "wlan_id2"
    }
  ]
}
```

