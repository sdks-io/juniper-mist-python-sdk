
# Response Inventory

## Structure

`ResponseInventory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added` | `List of string` | Optional | - |
| `duplicated` | `List of string` | Optional | - |
| `error` | `List of string` | Optional | - |
| `inventory_added` | [`List of InventoryAdded`](../../doc/models/inventory-added.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `inventory_duplicated` | [`List of InventoryDuplicated`](../../doc/models/inventory-duplicated.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

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
    },
    {
      "mac": "mac8",
      "magic": "magic4",
      "model": "model2",
      "serial": "serial4",
      "type": "type6"
    },
    {
      "mac": "mac9",
      "magic": "magic5",
      "model": "model3",
      "serial": "serial5",
      "type": "type5"
    }
  ]
}
```

