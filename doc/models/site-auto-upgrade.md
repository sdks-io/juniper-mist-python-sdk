
# Site Auto Upgrade

Auto Upgrade Settings

## Structure

`SiteAutoUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_versions` | `dict` | Optional | custom versions for different models. The property key is the model name (e.g. "AP41") |
| `day_of_week` | [`DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | - |
| `enabled` | `bool` | Optional | whether auto upgrade should happen (Note that Mist may auto-upgrade if the version is not supported)<br>**Default**: `False` |
| `time_of_day` | `string` | Optional | any / HH:MM (24-hour format), upgrade will happen within up to 1-hour from this time |
| `version` | [`Version2Enum`](../../doc/models/version-2-enum.md) | Optional | desired version<br>**Default**: `'stable'` |

## Example (as JSON)

```json
{
  "enabled": false,
  "version": "stable",
  "custom_versions": {
    "key0": "custom_versions3",
    "key1": "custom_versions4",
    "key2": "custom_versions5"
  },
  "day_of_week": "any",
  "time_of_day": "time_of_day6"
}
```

