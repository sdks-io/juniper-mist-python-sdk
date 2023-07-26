
# Mxedge 1

site mist edges form a cluster of radsecproxy servers

## Structure

`Mxedge1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mist_das` | [`MxedgeDas`](../../doc/models/mxedge-das.md) | Optional | configure cloud-assisted dynamic authorization service on this cluster of mist edges |
| `radsec` | [`MxclusterRadsec`](../../doc/models/mxcluster-radsec.md) | Optional | MxEdge Radsec Configuration |

## Example (as JSON)

```json
{
  "mist_das": {
    "coa_servers": [
      {
        "disable_event_timestamp_check": false,
        "enabled": false,
        "host": "host4",
        "port": 66,
        "secret": "secret8"
      },
      {
        "disable_event_timestamp_check": true,
        "enabled": true,
        "host": "host5",
        "port": 67,
        "secret": "secret9"
      }
    ],
    "enabled": false
  },
  "radsec": {
    "acct_servers": [
      {
        "host": "host5",
        "port": 163,
        "secret": "secret1",
        "ssids": [
          "ssids6",
          "ssids7"
        ]
      }
    ],
    "auth_servers": [
      {
        "host": "host9",
        "keywrap_enabled": true,
        "keywrap_format": "ascii",
        "keywrap_kek": "keywrap_kek5",
        "keywrap_mack": "keywrap_mack7"
      }
    ],
    "enabled": false,
    "match_ssid": false,
    "proxy_hosts": [
      "proxy_hosts4"
    ]
  }
}
```

