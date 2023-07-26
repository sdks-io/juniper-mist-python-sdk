
# Mxcluster Radsec

MxEdge Radsec Configuration

## Structure

`MxclusterRadsec`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_servers` | [`List of AcctServer1`](../../doc/models/acct-server-1.md) | Optional | list of RADIUS accounting servers, optional, order matters where the first one is treated as primary<br>**Constraints**: *Unique Items Required* |
| `auth_servers` | [`List of AuthServer1`](../../doc/models/auth-server-1.md) | Optional | list of RADIUS authentication servers, order matters where the first one is treated as primary<br>**Constraints**: *Unique Items Required* |
| `enabled` | `bool` | Optional | whether to enable service on Mist Edge i.e. RADIUS proxy over TLS |
| `match_ssid` | `bool` | Optional | whether to match ssid in request message to select from a subset of RADIUS servers |
| `proxy_hosts` | `List of string` | Optional | hostnames or IPs for Mist AP to use as the TLS Server (i.e. they are reachable from AP) in addition to `tunterm_hosts` |
| `server_selection` | [`ServerSelectionEnum`](../../doc/models/server-selection-enum.md) | Optional | ordered (default) / unordered. When ordered, Mist Edge will prefer and go back to the first radius server if possible<br>**Default**: `'ordered'` |
| `source` | [`SourceEnum`](../../doc/models/source-enum.md) | Optional | Specify source address to use when connecting to RADIUS servers<br>**Default**: `'any'` |

## Example (as JSON)

```json
{
  "server_selection": "ordered",
  "source": "any",
  "acct_servers": [
    {
      "host": "host1",
      "port": 15,
      "secret": "secret7",
      "ssids": [
        "ssids2",
        "ssids3"
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
    "proxy_hosts8"
  ]
}
```

