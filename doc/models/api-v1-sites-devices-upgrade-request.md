
# Api V1 Sites Devices Upgrade Request

## Structure

`ApiV1SitesDevicesUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reboot` | `bool` | Optional | Reboot device immediately after upgrade is completed (Available on Junos OS devices)<br>**Default**: `False` |
| `snapshot` | `bool` | Optional | Perform recovery snapshot after device is rebooted (Available on Junos OS devices)<br>**Default**: `False` |
| `version` | `string` | Required | specific `version` / `stable`, default is to use the latest<br>**Default**: `'stable'` |

## Example (as JSON)

```json
{
  "reboot": false,
  "snapshot": false,
  "version": "stable"
}
```

