
# Api V1 Sites Stats Switch Ports Search Response

## Structure

`ApiV1SitesStatsSwitchPortsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `results` | [`List of StatsSwitchPort`](../../doc/models/stats-switch-port.md) | Required | - |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "for_site": true,
      "mac": "mac7",
      "neighbor_mac": "neighbor_mac3",
      "neighbor_port_desc": "neighbor_port_desc7",
      "neighbor_system_name": "neighbor_system_name5",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "poe_disabled": true,
      "port_id": "port_id3",
      "port_mac": "port_mac3",
      "rx_bytes": 131,
      "rx_pkts": 189,
      "site_id": "00002183-0000-0000-0000-000000000000",
      "speed": 73,
      "tx_bytes": 13,
      "tx_pkts": 131
    }
  ],
  "start": 212,
  "total": 10
}
```

