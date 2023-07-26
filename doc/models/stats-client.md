
# Stats Client

Client statistics

## Structure

`StatsClient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ttl` | `float` | Required | TTL of the validity of the stat |
| `accuracy` | `int` | Optional | estimated clinet location accuracy, in meter |
| `airespace_ifname` | `string` | Optional | - |
| `airwatch` | [`Airwatch`](../../doc/models/airwatch.md) | Optional | information if airwatch enabled |
| `ap_id` | `uuid\|string` | Required | AP ID the client is connected to |
| `ap_mac` | `string` | Required | AP the client is connected to |
| `band` | [`Band7Enum`](../../doc/models/band-7-enum.md) | Required | - |
| `channel` | `int` | Required | current channel |
| `dual_band` | `bool` | Required | whether the client is dual-band capable (determined by whether we’ve seen probe requests from both bands) |
| `family` | `string` | Required | device family, through fingerprinting. iPod / Nexus Galaxy / Windows Mobile or CE … |
| `guest` | [`Guest1`](../../doc/models/guest-1.md) | Optional | information about this portal |
| `hostname` | `string` | Required | hostname that we learned from sniffing DHCP |
| `idle_time` | `float` | Required | how long, in seconds, has the client been idle (since the last RX packet) |
| `ip` | `string` | Required | - |
| `ip_6` | `string` | Optional | - |
| `is_guest` | `bool` | Required | whether this is a guest<br>**Default**: `False` |
| `key_mgmt` | `string` | Required | e.g. WPA2-PSK/CCMP |
| `last_seen` | `float` | Required | last seen timestamp |
| `mac` | `string` | Required | client mac |
| `manufacture` | `string` | Required | device manufacture, through fingerprinting or OUI |
| `map_id` | `uuid\|string` | Optional | estimated client location - map_id |
| `model` | `string` | Required | device model, may be available if we can identify them |
| `num_locating_aps` | `int` | Optional | number of APs used to locate this client |
| `os` | `string` | Required | device os, through fingerprinting |
| `power_saving` | `bool` | Required | if it’s currently in power-save mode |
| `proto` | [`Proto1Enum`](../../doc/models/proto-1-enum.md) | Required | - |
| `psk_id` | `uuid\|string` | Optional | PSK id (if multi-psk is used) |
| `rssi` | `float` | Required | signal strength |
| `rx_bps` | `float` | Required | rate of receiving traffic from the clients, bits/seconds, last known |
| `rx_bytes` | `float` | Required | amount of traffic received from client since client connects |
| `rx_packets` | `float` | Required | amount of traffic received from client since client connects |
| `rx_rate` | `float` | Required | RX Rate, Mbps |
| `rx_retries` | `float` | Required | amount of rx retries |
| `snr` | `float` | Required | signal over noise |
| `ssid` | `string` | Required | SSID the client is connected to |
| `tx_bps` | `float` | Required | rate of transmitting traffic to the clients, bits/seconds, last known |
| `tx_bytes` | `float` | Required | amount of traffic sent to client since client connects |
| `tx_packets` | `float` | Required | amount of traffic sent to client since client connects |
| `tx_rate` | `float` | Required | TX Rate, Mbps |
| `tx_retries` | `float` | Required | amount of tx retries |
| `mtype` | `string` | Optional | client’s type, regular / vip / resource / blocked (if client object is created) |
| `uptime` | `float` | Required | how long, in seconds, has the client been connected |
| `username` | `string` | Required | username that we learned from 802.1X exchange or Per-user PSK or User Portal |
| `vlan_id` | `int` | Optional | vlan id, could be empty (from older AP) |
| `wlan_id` | `uuid\|string` | Required | WLAN ID the client is connected to |
| `x` | `float` | Optional | estimated client location in pixels |
| `x_m` | `float` | Optional | estimated client location in meter |
| `y` | `float` | Optional | estimated client location in pixels |
| `y_m` | `float` | Optional | estimated client location in meter |

## Example (as JSON)

```json
{
  "_ttl": 179.16,
  "ap_id": "000017be-0000-0000-0000-000000000000",
  "ap_mac": "ap_mac2",
  "band": "24",
  "channel": 120,
  "dual_band": false,
  "family": "family2",
  "hostname": "hostname4",
  "idle_time": 43.72,
  "ip": "ip4",
  "is_guest": false,
  "key_mgmt": "key_mgmt2",
  "last_seen": 33.7,
  "mac": "mac4",
  "manufacture": "manufacture4",
  "model": "model2",
  "os": "os8",
  "power_saving": false,
  "proto": "a",
  "rssi": 2.78,
  "rx_bps": 103.9,
  "rx_bytes": 255.58,
  "rx_packets": 126.12,
  "rx_rate": 67.0,
  "rx_retries": 33.78,
  "snr": 133.04,
  "ssid": "ssid2",
  "tx_bps": 76.04,
  "tx_bytes": 121.28,
  "tx_packets": 139.14,
  "tx_rate": 48.76,
  "tx_retries": 108.58,
  "uptime": 141.3,
  "username": "username0",
  "wlan_id": "00002208-0000-0000-0000-000000000000",
  "accuracy": 186,
  "airespace_ifname": "airespace_ifname0",
  "airwatch": {
    "authorized": false
  },
  "guest": {
    "authorized": false,
    "authorized_expiring_time": 236.54,
    "authorized_time": 42.96,
    "company": "company2",
    "email": "email4",
    "field1": "field16",
    "name": "name2"
  },
  "ip6": "ip60"
}
```

