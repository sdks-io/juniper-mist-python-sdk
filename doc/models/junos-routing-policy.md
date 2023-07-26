
# Junos Routing Policy

## Structure

`JunosRoutingPolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terms` | [`List of Term`](../../doc/models/term.md) | Optional | zero or more criteria/filter can be specified to match the term, all criteria have to be met<br>**Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "terms": [
    {
      "action": {
        "accept": true,
        "add_community": [
          "add_community2"
        ],
        "community": [
          "community3",
          "community4"
        ],
        "exclude_as_path": [
          "exclude_as_path1"
        ],
        "exclude_community": [
          "exclude_community6",
          "exclude_community7",
          "exclude_community8"
        ]
      },
      "matching": {
        "as_path": [
          "as_path1",
          "as_path2",
          "as_path3"
        ],
        "community": [
          "community9",
          "community0",
          "community1"
        ],
        "network": [
          "network8"
        ],
        "prefix": [
          "prefix6"
        ],
        "protocol": [
          "protocol6",
          "protocol7",
          "protocol8"
        ]
      }
    },
    {
      "action": {
        "accept": false,
        "add_community": [
          "add_community1",
          "add_community2",
          "add_community3"
        ],
        "community": [
          "community4",
          "community5",
          "community6"
        ],
        "exclude_as_path": [
          "exclude_as_path2",
          "exclude_as_path3"
        ],
        "exclude_community": [
          "exclude_community5",
          "exclude_community6"
        ]
      },
      "matching": {
        "as_path": [
          "as_path0",
          "as_path1"
        ],
        "community": [
          "community8",
          "community9"
        ],
        "network": [
          "network7",
          "network8",
          "network9"
        ],
        "prefix": [
          "prefix7",
          "prefix8"
        ],
        "protocol": [
          "protocol7"
        ]
      }
    },
    {
      "action": {
        "accept": true,
        "add_community": [
          "add_community0",
          "add_community1"
        ],
        "community": [
          "community5"
        ],
        "exclude_as_path": [
          "exclude_as_path3",
          "exclude_as_path4",
          "exclude_as_path5"
        ],
        "exclude_community": [
          "exclude_community4"
        ]
      },
      "matching": {
        "as_path": [
          "as_path9"
        ],
        "community": [
          "community7"
        ],
        "network": [
          "network6",
          "network7"
        ],
        "prefix": [
          "prefix8",
          "prefix9",
          "prefix0"
        ],
        "protocol": [
          "protocol8",
          "protocol9"
        ]
      }
    }
  ]
}
```

