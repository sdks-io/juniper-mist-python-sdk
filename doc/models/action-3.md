
# Action 3

when used as import policy

## Structure

`Action3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `bool` | Optional | - |
| `add_community` | `List of string` | Optional | - |
| `community` | `List of string` | Optional | when used as export policy, optional |
| `exclude_as_path` | `List of string` | Optional | when used as export policy, optional. To exclude certain AS |
| `exclude_community` | `List of string` | Optional | - |
| `export_communitites` | `List of string` | Optional | when used as export policy, optional |
| `local_preference` | `string` | Optional | optional, for an import policy, local_preference can be changed |
| `prepend_as_path` | `List of string` | Optional | when used as export policy, optional. By default, the local AS will be prepended, to change it |

## Example (as JSON)

```json
{
  "accept": false,
  "add_community": [
    "add_community1"
  ],
  "community": [
    "community8",
    "community9"
  ],
  "exclude_as_path": [
    "exclude_as_path6"
  ],
  "exclude_community": [
    "exclude_community1",
    "exclude_community2",
    "exclude_community3"
  ]
}
```

