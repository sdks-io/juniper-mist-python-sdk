
# Secondary 1

## Structure

`Secondary1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hosts` | `List of string` | Optional | - |
| `internal_ips` | `List of string` | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `probe_ips` | `List of string` | Optional | - |
| `remote_ids` | `List of string` | Optional | Only if:<br><br>* `provider`== `custom-ipsec` |
| `wan_names` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "hosts": [
    "hosts1"
  ],
  "internal_ips": [
    "internal_ips8",
    "internal_ips9"
  ],
  "probe_ips": [
    "probe_ips1"
  ],
  "remote_ids": [
    "remote_ids1"
  ],
  "wan_names": [
    "wan_names2",
    "wan_names3"
  ]
}
```

