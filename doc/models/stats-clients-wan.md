
# Stats Clients Wan

## Structure

`StatsClientsWan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `when` | `string` | Optional | - |
| `hostname` | `List of string` | Optional | - |
| `ip` | `List of string` | Optional | - |
| `last_hostname` | `string` | Optional | - |
| `last_ip` | `string` | Optional | - |
| `mfg` | `string` | Optional | - |
| `org_id` | `string` | Optional | - |
| `site_id` | `string` | Optional | - |
| `wcid` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "When": "12/31/2022 23:59:43",
  "last_hostname": "sonoszp",
  "last_ip": "192.168.1.139",
  "mfg": "Sonos",
  "org_id": "b4e16c72-d50e-4c03-a952-a3217e231e2c",
  "site_id": "f688779c-e335-4f88-8d7c-9c5e9964528b",
  "wcid": "8bbe7389-212b-c65d-2208-00fab2017936",
  "hostname": [
    "hostname2",
    "hostname3",
    "hostname4"
  ],
  "ip": [
    "ip1",
    "ip2"
  ]
}
```

