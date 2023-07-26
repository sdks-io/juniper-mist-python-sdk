
# License

License

## Structure

`License`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amendments` | [`List of Amendment`](../../doc/models/amendment.md) | Optional | **Constraints**: *Unique Items Required* |
| `entitled` | `dict` | Optional | Property key is license type (e.g. SUB-MAN)  and Property value is the number of licenses entitled. |
| `licenses` | [`List of License1`](../../doc/models/license-1.md) | Optional | list of registered licenses<br>**Constraints**: *Unique Items Required* |
| `summary` | `dict` | Optional | Property key is license type (e.g. SUB-MAN) and Property value is the number of licenses consumed. |

## Example (as JSON)

```json
{
  "amendments": [
    {
      "created_time": 100.17,
      "end_time": 11,
      "id": "id7",
      "modified_time": 21.21,
      "quantity": 239
    }
  ],
  "entitled": {
    "key0": 50
  },
  "licenses": [
    {
      "created_time": 51.97,
      "end_time": 55,
      "id": "00000a07-0000-0000-0000-000000000000",
      "modified_time": 26.99,
      "order_id": "order_id1"
    }
  ],
  "summary": {
    "key0": 248,
    "key1": 249,
    "key2": 250
  }
}
```

