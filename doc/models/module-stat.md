
# Module Stat

## Structure

`ModuleStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | used to report all error states the device node is running into.<br>An error should always have `type` and `since` fields, and could have some other fields specific to that type. |
| `fans` | [`List of Fan`](../../doc/models/fan.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `model` | `string` | Optional | - |
| `poe` | [`Poe`](../../doc/models/poe.md) | Optional | - |
| `psus` | [`List of Psu`](../../doc/models/psu.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `serial` | `string` | Optional | - |
| `temperatures` | [`List of Temperature`](../../doc/models/temperature.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `vc_links` | [`List of VcLink`](../../doc/models/vc-link.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `vc_role` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "errors": [
    {
      "feature": "feature9",
      "minimum_version": "minimum_version7",
      "reason": "reason9",
      "since": 181,
      "type": "type5"
    },
    {
      "feature": "feature8",
      "minimum_version": "minimum_version8",
      "reason": "reason8",
      "since": 182,
      "type": "type4"
    },
    {
      "feature": "feature7",
      "minimum_version": "minimum_version9",
      "reason": "reason7",
      "since": 183,
      "type": "type3"
    }
  ],
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

