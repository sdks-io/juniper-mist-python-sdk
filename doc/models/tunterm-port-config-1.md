
# Tunterm Port Config 1

## Structure

`TuntermPortConfig1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `downstream_ports` | `List of object` | Optional | - |
| `separate_upstream_downstream` | `bool` | Optional | - |
| `upstream_ports` | `List of object` | Optional | - |

## Example (as JSON)

```json
{
  "downstream_ports": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "separate_upstream_downstream": false,
  "upstream_ports": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ]
}
```

