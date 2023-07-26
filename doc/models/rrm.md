
# Rrm

RRM

## Structure

`Rrm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band_24` | [`dict`](../../doc/models/rrm-band.md) | Required | proposal on band 2.4G, key is ap_id, value is the proposal |
| `band_24_metric` | [`RrmBandMetric`](../../doc/models/rrm-band-metric.md) | Required | - |
| `band_5` | [`dict`](../../doc/models/rrm-band.md) | Required | proposal on band 5G, key is ap_id, value is the proposal |
| `band_5_metric` | [`RrmBandMetric`](../../doc/models/rrm-band-metric.md) | Required | - |
| `band_6` | [`dict`](../../doc/models/rrm-band.md) | Optional | proposal on band 6G, key is ap_id, value is the proposal |
| `band_6_metric` | [`RrmBandMetric`](../../doc/models/rrm-band-metric.md) | Optional | - |
| `rftemplate` | [`Rftemplate`](../../doc/models/rftemplate.md) | Required | RF Template |
| `rftemplate_id` | `uuid\|string` | Required | - |
| `rftemplate_name` | `string` | Required | - |
| `status` | [`Status3Enum`](../../doc/models/status-3-enum.md) | Required | - |
| `timestamp` | `float` | Required | time where the status was updated |

## Example (as JSON)

```json
{
  "band_24": {
    "key0": {
      "bandwidth": 20,
      "channel": 228,
      "curr_bandwidht": 80,
      "curr_channel": 92,
      "curr_power": 224
    },
    "key1": {
      "bandwidth": 40,
      "channel": 227,
      "curr_bandwidht": 160,
      "curr_channel": 91,
      "curr_power": 225
    }
  },
  "band_24_metric": {
    "cochannel_neighbors": 161.38,
    "density": 107.0,
    "neighbors": 12.0,
    "noise": 252.7
  },
  "band_5": {
    "key0": {
      "bandwidth": 80,
      "channel": 246,
      "curr_bandwidht": 20,
      "curr_channel": 126,
      "curr_power": 186
    },
    "key1": {
      "bandwidth": 160,
      "channel": 247,
      "curr_bandwidht": 40,
      "curr_channel": 127,
      "curr_power": 187
    },
    "key2": {
      "bandwidth": 20,
      "channel": 248,
      "curr_bandwidht": 80,
      "curr_channel": 128,
      "curr_power": 188
    }
  },
  "band_5_metric": {
    "cochannel_neighbors": 78.16,
    "density": 23.78,
    "neighbors": 184.78,
    "noise": 86.52
  },
  "rftemplate": {
    "band_24_usage": "24",
    "name": "name6",
    "ant_gain_24": 220,
    "ant_gain_5": 132,
    "band_24": {
      "allow_rrm_disable": false,
      "ant_gain": 12,
      "antenna_mode": "4x4",
      "bandwidth": 20,
      "channel": 92
    },
    "band_5": {
      "allow_rrm_disable": false,
      "ant_gain": 16,
      "antenna_mode": "3x3",
      "bandwidth": 20,
      "channel": 192
    }
  },
  "rftemplate_id": "00002648-0000-0000-0000-000000000000",
  "rftemplate_name": "rftemplate_name2",
  "status": "ready",
  "timestamp": 128.82,
  "band_6": {
    "key0": {
      "bandwidth": 20,
      "channel": 240,
      "curr_bandwidht": 80,
      "curr_channel": 104,
      "curr_power": 212
    },
    "key1": {
      "bandwidth": 40,
      "channel": 239,
      "curr_bandwidht": 160,
      "curr_channel": 103,
      "curr_power": 213
    }
  },
  "band_6_metric": {
    "cochannel_neighbors": 154.0,
    "density": 99.62,
    "neighbors": 4.62,
    "noise": 10.68
  }
}
```

