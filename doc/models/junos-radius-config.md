
# Junos Radius Config

Junos Radius config

## Structure

`JunosRadiusConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_interim_interval` | `int` | Optional | how frequently should interim accounting be reported, 60-65535. default is 0 (use one specified in Access-Accept request from RADIUS Server). Very frequent messages can affect the performance of the radius server, 600 and up is recommended when enabled<br>**Default**: `0`<br>**Constraints**: `>= 0`, `<= 65535` |
| `acct_servers` | [`List of AcctServer`](../../doc/models/acct-server.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `auth_servers` | [`List of AuthServer`](../../doc/models/auth-server.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `auth_servers_retries` | `int` | Optional | radius auth session retries<br>**Default**: `3` |
| `auth_servers_timeout` | `int` | Optional | radius auth session timeout<br>**Default**: `5` |
| `coa_enabled` | `bool` | Optional | **Default**: `False` |
| `coa_port` | `int` | Optional | **Default**: `3799` |
| `network` | `string` | Optional | use `network`or `source_ip`<br>which network the RADIUS server resides, if there's static IP for this network, we'd use it as source-ip |
| `source_ip` | `string` | Optional | use `network`or `source_ip` |

## Example (as JSON)

```json
{
  "acct_interim_interval": 0,
  "auth_servers_retries": 3,
  "auth_servers_timeout": 5,
  "coa_enabled": false,
  "coa_port": 3799,
  "acct_servers": [
    {
      "host": "host1",
      "keywrap_enabled": true,
      "keywrap_format": "keywrap_format5",
      "keywrap_kek": "keywrap_kek3",
      "keywrap_mack": "keywrap_mack5",
      "port": 15,
      "secret": "secret7"
    }
  ],
  "auth_servers": [
    {
      "host": "host9",
      "keywrap_enabled": true,
      "keywrap_format": "keywrap_format3",
      "keywrap_kek": "keywrap_kek5",
      "keywrap_mack": "keywrap_mack7",
      "port": 73,
      "secret": "secret5"
    }
  ]
}
```

