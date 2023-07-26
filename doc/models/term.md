
# Term

## Structure

`Term`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action3`](../../doc/models/action-3.md) | Optional | when used as import policy |
| `matching` | [`Matching1`](../../doc/models/matching-1.md) | Optional | zero or more criteria/filter can be specified to match the term, all criteria have to be met |

## Example (as JSON)

```json
{
  "action": {
    "accept": false,
    "add_community": [
      "add_community9"
    ],
    "community": [
      "community8",
      "community9",
      "community0"
    ],
    "exclude_as_path": [
      "exclude_as_path4"
    ],
    "exclude_community": [
      "exclude_community3",
      "exclude_community4",
      "exclude_community5"
    ]
  },
  "matching": {
    "as_path": [
      "as_path2"
    ],
    "community": [
      "community4"
    ],
    "network": [
      "network7",
      "network8",
      "network9"
    ],
    "prefix": [
      "prefix5",
      "prefix6",
      "prefix7"
    ],
    "protocol": [
      "protocol5",
      "protocol6"
    ]
  }
}
```

