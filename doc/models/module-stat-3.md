
# Module Stat 3

## Structure

`ModuleStat3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fans` | [`List of Fan`](../../doc/models/fan.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `model` | `string` | Optional | - |
| `pics` | [`Pics`](../../doc/models/pics.md) | Optional | - |
| `poe` | [`Poe`](../../doc/models/poe.md) | Optional | - |
| `psus` | [`List of Psu`](../../doc/models/psu.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `serial` | `string` | Optional | - |
| `temperatures` | [`List of Temperature`](../../doc/models/temperature.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `vc_links` | [`List of VcLink`](../../doc/models/vc-link.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `vc_role` | `string` | Optional | - |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | used to report all error states the device node is running into.<br>An error should always have `type` and `since` fields, and could have some other fields specific to that type. |

## Example (as JSON)

```json
{
  "fans": [
    {
      "airflow": "airflow6",
      "name": "name2",
      "status": "status6"
    },
    {
      "airflow": "airflow7",
      "name": "name3",
      "status": "status5"
    }
  ],
  "model": "model2",
  "pics": {
    "idx": 100,
    "port_groups": [
      {
        "count": 72,
        "type": "type0"
      },
      {
        "count": 71,
        "type": "type9"
      },
      {
        "count": 70,
        "type": "type8"
      }
    ]
  },
  "poe": {
    "max_power": 232.0,
    "power_draw": 236.74
  },
  "psus": [
    {
      "name": "name7",
      "status": "status1"
    },
    {
      "name": "name8",
      "status": "status0"
    }
  ]
}
```

