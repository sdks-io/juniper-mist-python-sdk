
# Api V1 Sites Ssr Upgrade Request

## Structure

`ApiV1SitesSsrUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel` | [`ChannelEnum`](../../doc/models/channel-enum.md) | Optional | upgrade channel to follow<br>**Default**: `'stable'` |
| `reboot_at` | `int` | Optional | eboot start time in epoch seconds, default is start_time, -1 disables reboot |
| `start_time` | `int` | Optional | 128T firmware download start time in epoch seconds, default is now, -1 disables download |
| `version` | `string` | Required | 128T firmware version to upgrade (e.g. 5.3.0-93)<br>**Default**: `'stable'`<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "channel": "stable",
  "version": "stable",
  "reboot_at": 190,
  "start_time": 120
}
```

