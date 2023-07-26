
# Claim License

## Structure

`ClaimLicense`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `inventory_added` | [`List of InventoryAdded`](../../doc/models/inventory-added.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `inventory_duplicated` | [`List of InventoryDuplicated`](../../doc/models/inventory-duplicated.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `license_added` | [`List of LicenseAdded`](../../doc/models/license-added.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `license_duplicated` | [`List of LicenseDuplicated`](../../doc/models/license-duplicated.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `license_error` | [`List of LicenseError`](../../doc/models/license-error.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
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
  ],
  "license_added": [
    {
      "end": 30,
      "quantity": 100,
      "start": 244,
      "type": "type4"
    }
  ],
  "license_duplicated": [
    {
      "end": 156,
      "quantity": 226,
      "start": 114,
      "type": "type2"
    }
  ],
  "license_error": [
    {
      "order": "order9",
      "reason": "reason7"
    }
  ]
}
```

