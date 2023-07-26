
# Org Device Upgrade Response

## Structure

`OrgDeviceUpgradeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_p_2_p` | `bool` | Optional | whether to allow local AP-to-AP FW upgrade |
| `force` | `bool` | Optional | whether to force upgrade when requested version is same as running version |
| `id` | `uuid\|string` | Required | unique id for the upgrade |
| `start_time` | `float` | Optional | upgrade start time in epoch |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | status upgrade is in |
| `strategy` | [`Strategy1Enum`](../../doc/models/strategy-1-enum.md) | Optional | upgrade strategy<br>**Default**: `'big_bang'`<br>**Constraints**: *Minimum Length*: `1` |
| `target_version` | `string` | Optional | version to upgrade to<br>**Constraints**: *Minimum Length*: `1` |
| `upgrades` | [`List of Upgrade`](../../doc/models/upgrade.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "00001770-0000-0000-0000-000000000000",
  "strategy": "big_bang",
  "enable_p2p": false,
  "force": false,
  "start_time": 195.76,
  "status": "created"
}
```

