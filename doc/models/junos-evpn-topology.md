
# Junos Evpn Topology

## Structure

`JunosEvpnTopology`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `pod_names` | `dict` | Optional | Property key is the pod number |
| `switches` | [`List of Switches1`](../../doc/models/switches-1.md) | Required | **Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "switches": [
    {
      "deviceprofile_id": "6a1deab1-96df-4fa2-8455-d5253f943d06",
      "pod": 1,
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "downlink_ips": [
        "downlink_ips5",
        "downlink_ips6"
      ],
      "downlinks": [
        "downlinks3"
      ],
      "esilaglinks": [
        "esilaglinks3"
      ],
      "evpn_id": 49
    }
  ],
  "id": "id0",
  "name": "name0",
  "pod_names": {
    "key0": "pod_names8",
    "key1": "pod_names9",
    "key2": "pod_names0"
  }
}
```

