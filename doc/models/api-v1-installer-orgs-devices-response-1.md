
# Api V1 Installer Orgs Devices Response 1

## Structure

`ApiV1InstallerOrgsDevicesResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added` | `List of string` | Required | - |
| `duplicated` | `List of string` | Required | - |
| `error` | `List of string` | Required | - |
| `inventory_added` | [`List of InventoryAdded`](../../doc/models/inventory-added.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `inventory_duplicated` | [`List of InventoryDuplicated`](../../doc/models/inventory-duplicated.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "added": [
    "added8",
    "added9",
    "added0"
  ],
  "duplicated": [
    "duplicated7",
    "duplicated8"
  ],
  "error": [
    "error1"
  ],
  "inventory_added": [
    {
      "mac": "mac7",
      "magic": "magic3",
      "model": "model1",
      "serial": "serial3",
      "type": "type7"
    }
  ],
  "inventory_duplicated": [
    {
      "mac": "mac7",
      "magic": "magic3",
      "model": "model1",
      "serial": "serial3",
      "type": "type7"
    }
  ]
}
```

