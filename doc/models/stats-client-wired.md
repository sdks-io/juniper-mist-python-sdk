
# Stats Client Wired

## Structure

`StatsClientWired`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `ttl` | `float` | Optional | TTL of the validity of the stat |
| `auth_state` | `string` | Optional | client authorization status<br>**Constraints**: *Minimum Length*: `1` |
| `device_id` | `string` | Optional | Device ID the client is connected to<br>**Constraints**: *Minimum Length*: `1` |
| `eth_port` | `string` | Optional | port on AP where the wired client is connected<br>**Constraints**: *Minimum Length*: `1` |
| `last_seen` | `float` | Optional | time when last Tx/Rx observed |
| `mac` | `string` | Required | client mac<br>**Constraints**: *Minimum Length*: `1` |
| `rx_bytes` | `float` | Optional | amount of traffic sent to client since client connects |
| `rx_pkts` | `float` | Optional | amount of traffic sent to client since client connects |
| `site_id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `tx_bytes` | `float` | Optional | amount of traffic received from client since client connects |
| `tx_pkts` | `float` | Optional | amount of traffic received from client since client connects |
| `uptime` | `float` | Optional | how long, in seconds, has the client been connected |
| `vlan_id` | `float` | Optional | vlan id, could be empty |

## Example (as JSON)

```json
{
  "_id": "_id4",
  "_ttl": 179.16,
  "auth_state": "auth_state0",
  "device_id": "device_id6",
  "eth_port": "eth_port8",
  "mac": "mac4"
}
```

