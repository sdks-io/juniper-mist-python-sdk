
# Webhook Asset Raw

asset raw webhook

## Structure

`WebhookAssetRaw`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event1`](../../doc/models/event-1.md) | Required | list of events<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | topic subscribed to<br>**Default**: `'asset-raw'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "asset_id": "00000374-0000-0000-0000-000000000000",
      "beam": 146,
      "device_id": "00000380-0000-0000-0000-000000000000",
      "ibeacon_major": 200,
      "ibeacon_minor": 62,
      "ibeacon_uuid": "00000d30-0000-0000-0000-000000000000",
      "mac": "mac4",
      "map_id": "00000c02-0000-0000-0000-000000000000",
      "mfg_company_id": 35.84,
      "mfg_data": "mfg_data2",
      "rssi": 27.72,
      "service_data_data": "service_data_data8",
      "service_data_last_rx_time": 188,
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 157.68
    }
  ],
  "topic": "asset-raw"
}
```

